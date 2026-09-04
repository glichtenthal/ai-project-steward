#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
output=${1:-"$repo_root/dist/ai-project-steward.skill"}

case "$output" in
  /*) ;;
  *) output="$repo_root/$output" ;;
esac

mkdir -p "$(dirname "$output")"
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
package_root="$stage/ai-project-steward"
verify_root="$stage/verify"
mkdir -p "$package_root" "$verify_root"

while IFS= read -r -d '' file; do
  mkdir -p "$package_root/$(dirname "$file")"
  cp "$repo_root/$file" "$package_root/$file"
done < <(git -C "$repo_root" ls-files -z)

rm -f "$output"
(
  cd "$stage"
  zip -X -q -r "$output" ai-project-steward
)

unzip -q "$output" -d "$verify_root"
tracked_count=0
while IFS= read -r -d '' file; do
  cmp "$repo_root/$file" "$verify_root/ai-project-steward/$file"
  tracked_count=$((tracked_count + 1))
done < <(git -C "$repo_root" ls-files -z)

archive_count=$(unzip -Z1 "$output" | awk '!/\/$/ { count += 1 } END { print count + 0 }')
if [[ "$archive_count" -ne "$tracked_count" ]]; then
  printf 'Archive contains %s files; expected %s tracked files.\n' "$archive_count" "$tracked_count" >&2
  exit 1
fi

printf 'Release archive verified: %s tracked files\n' "$tracked_count"
printf 'Artifact: %s\n' "$output"
shasum -a 256 "$output"
