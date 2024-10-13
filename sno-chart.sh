#!/bin/bash

apt -y update && apt -y install jq

# Ensure we are inside a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "This script must be run inside a git repository."
  exit 1
fi

# Iterate over each commit that modified the custom-node-list.json file
git log --format='%H %ad' --date=format:'%Y-%m-%d' -- custom-node-list.json | while read commit_hash commit_date; do
  # Output the file content at the specific commit into a new file named cn-$commit_date.json
  output_file="cn-$commit_date.json"

  # Checkout the file content specific to the historical commit
  git show "$commit_hash:custom-node-list.json" > "$output_file"

  echo "Extracted version from $commit_date into $output_file"
done


# for each cn-*.json, run "cat $output_file | jq '.custom_nodes | length'", append output to length.csv

# Initialize the output file
echo "Filename,Custom_Nodes_Length" > length.csv

# Loop through each file matching the pattern cn-*.json
for json_file in cn-*.json; do
  # Check if the file exists to avoid errors when no match is found
  if [[ -f $json_file ]]; then
    # Run jq to find the length of .custom_nodes in the JSON file
    length=$(jq '.custom_nodes | length' "$json_file" 2>/dev/null)
    
    # Append filename and length to the CSV file
    echo "$json_file,$length" >> length.csv
  fi
done

echo "Results have been saved to length.csv"
