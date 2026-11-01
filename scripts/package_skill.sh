#!/usr/bin/env bash
set -euo pipefail
repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
output=${1:-"$repo_root/dist/ai-project-steward.skill"}
case "$output" in /*) ;; *) output="$repo_root/$output" ;; esac
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
expected="$stage/expected.txt"
: > "$expected"
while IFS= read -r file || [[ -n "$file" ]]; do
  case "$file" in ''|\#*) continue ;; esac
  if [[ ! "$file" =~ ^[A-Za-z0-9_./-]+$ ]] || [[ "$file" == /* ]] || [[ "/$file/" == *'/../'* ]] || [[ "/$file/" == *'/./'* ]] || [[ "$file" == *'//'* ]]; then
    printf 'Unsafe manifest entry: %s\n' "$file" >&2; exit 1
  fi
  git -C "$repo_root" ls-files --error-unmatch -- "$file" >/dev/null
  [[ -f "$repo_root/$file" && ! -L "$repo_root/$file" ]] || { printf 'Missing or linked file: %s\n' "$file" >&2; exit 1; }
  parent=$(dirname "$file")
  while [[ "$parent" != '.' ]]; do
    [[ ! -L "$repo_root/$parent" ]] || { printf 'Linked directory: %s\n' "$parent" >&2; exit 1; }
    parent=$(dirname "$parent")
  done
  printf '%s\n' "$file" >> "$expected"
done < "$repo_root/distribution-manifest.txt"
[[ -s "$expected" ]] || { printf 'Empty distribution manifest\n' >&2; exit 1; }
LC_ALL=C sort "$expected" > "$stage/sorted.txt"
[[ $(LC_ALL=C sort -u "$expected" | wc -l) -eq $(wc -l < "$expected") ]] || { printf 'Duplicate manifest entry\n' >&2; exit 1; }
while IFS= read -r file; do
  mkdir -p "$stage/ai-project-steward/$(dirname "$file")"
  cp "$repo_root/$file" "$stage/ai-project-steward/$file"
  TZ=UTC touch -t 200001010000 "$stage/ai-project-steward/$file"
  printf 'ai-project-steward/%s\n' "$file" >> "$stage/zip-list.txt"
done < "$stage/sorted.txt"
mkdir -p "$(dirname "$output")"
# Build outside the destination so a rejected manifest cannot overwrite a prior artifact.
(cd "$stage" && zip -X -q package.skill -@ < zip-list.txt)
unzip -Z1 "$stage/package.skill" | sed 's|^ai-project-steward/||' | LC_ALL=C sort > "$stage/actual.txt"
cmp "$stage/sorted.txt" "$stage/actual.txt"
unzip -q "$stage/package.skill" -d "$stage/verify"
while IFS= read -r file; do
  cmp "$repo_root/$file" "$stage/verify/ai-project-steward/$file"
done < "$stage/sorted.txt"
mv "$stage/package.skill" "$output"
printf 'Distribution verified: %s manifest files; exact membership and byte parity\n' "$(wc -l < "$expected" | tr -d ' ')"
printf 'Artifact: %s\n' "$output"
shasum -a 256 "$output"
