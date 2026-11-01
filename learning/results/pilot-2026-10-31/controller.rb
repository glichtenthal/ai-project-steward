require 'json'
require 'fileutils'
root=Dir.pwd # run only in a prepared local pilot workspace, never from CI
jobs=Dir.glob(File.join(root,'pilot/private/*/{baseline,candidate}')).sort
queue=Queue.new
jobs.each{|d| queue << d unless File.exist?(File.join(d,'execution.json'))}
threads=3.times.map do
 Thread.new do
  loop do
   begin;dir=queue.pop(true);rescue ThreadError;break;end
   start=Time.now
   out=File.open(File.join(dir,'events.jsonl'),'w');err=File.open(File.join(dir,'stderr.txt'),'w');input=File.open(File.join(dir,'prompt.txt'))
   args=['codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--sandbox','read-only','-m','gpt-6.1-sol','-c','model_reasoning_effort="high"','--json','-C',dir,'-o',File.join(dir,'output.md'),'-']
   pid=Process.spawn(*args,in:input,out:out,err:err,pgroup:true)
   timed=false;status=nil
   loop do
    r=Process.waitpid2(pid,Process::WNOHANG)
    if r;status=r[1];break;end
    if Time.now-start>120
     timed=true;Process.kill('TERM',-pid) rescue nil;sleep 1;Process.kill('KILL',-pid) rescue nil
     _,status=Process.waitpid2(pid);break
    end
    sleep 0.25
   end
   [out,err,input].each(&:close)
   usage=File.readlines(File.join(dir,'events.jsonl')).map{|l| begin;x=JSON.parse(l);x['usage'] if x['type']=='turn.completed';rescue JSON::ParserError;nil;end}.compact.last
   record={elapsed_seconds:(Time.now-start).round(3),exit_code:status.exitstatus,timeout:timed,model:'gpt-6.1-sol',reasoning:'high',harness:'codex-cli 0.166.0-alpha.5.1',sandbox:'read-only',usage:usage,command:args}
   File.write(File.join(dir,'execution.json'),JSON.pretty_generate(record)+"\n")
   puts "#{dir.delete_prefix(root+'/pilot/private/')} #{record[:exit_code]} #{record[:elapsed_seconds]}s";STDOUT.flush
  end
 end
end
threads.each(&:join)
