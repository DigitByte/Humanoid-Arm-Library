#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
components_dir="$repo_root/components"
catalog_file="$components_dir/CATALOG.md"

if [[ ! -d "$components_dir" ]]; then
  echo "components directory not found: $components_dir" >&2
  exit 1
fi

# Collect rows as: id|name|category|status|path
rows=()
while IFS= read -r yaml_file; do
  id="$(awk -F': ' '/^id:/ {print $2; exit}' "$yaml_file" | xargs)"
  name="$(awk -F': ' '/^name:/ {print $2; exit}' "$yaml_file" | xargs)"
  category="$(awk -F': ' '/^category:/ {print $2; exit}' "$yaml_file" | xargs)"
  status="$(awk -F': ' '/^status:/ {print $2; exit}' "$yaml_file" | xargs)"
  rel_dir="${yaml_file#$repo_root/}"
  rel_dir="${rel_dir%/component.yaml}/"

  [[ -n "$id" ]] || id="UNKNOWN"
  [[ -n "$name" ]] || name="UNKNOWN"
  [[ -n "$category" ]] || category="UNKNOWN"
  [[ -n "$status" ]] || status="UNKNOWN"

  rows+=("$id|$name|$category|$status|$rel_dir")
done < <(find "$components_dir" -name component.yaml -type f | sort)

# Sort rows by ID for stable output
IFS=$'\n' sorted_rows=($(printf '%s\n' "${rows[@]}" | sort))
unset IFS

{
  echo "# Components Catalog"
  echo
  echo "Canonical index of reusable humanoid arm library components."
  echo
  echo "| ID | Name | Category | Status | Path |"
  echo "|---|---|---|---|---|"

  for row in "${sorted_rows[@]}"; do
    IFS='|' read -r id name category status rel_dir <<< "$row"
    unset IFS
    echo "| \`$id\` | $name | $category | $status | \`$rel_dir\` |"
  done

  echo
  echo "## Usage"
  echo
  echo "1. Pick components by ID from this table."
  echo "2. Use component folders for interface and CAD references."
  echo "3. Compose assemblies under \`assemblies/\` using these IDs."
} > "$catalog_file"

echo "Updated: $catalog_file"
