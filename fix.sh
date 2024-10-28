#!/bin/bash

# Define an array of maps with target directories as keys and space-separated URLs as values
declare -A targets
targets["cardiffnlp/twitter-roberta-base-offensive"]="https://huggingface.co/cardiffnlp/twitter-roberta-base-irony/resolve/main/merges.txt https://huggingface.co/cardiffnlp/twitter-roberta-base-irony/resolve/main/vocab.json"
targets["cardiffnlp/twitter-roberta-base-irony"]="https://huggingface.co/cardiffnlp/twitter-roberta-base-irony/resolve/main/merges.txt https://huggingface.co/cardiffnlp/twitter-roberta-base-irony/resolve/main/vocab.json"

# Loop through the array of maps
for target_dir in "${!targets[@]}"; do
    # Check if the target directory exists
    if [ -d "$target_dir" ]; then
        # Split the URLs string into an array
        IFS=' ' read -r -a urls <<< "${targets[$target_dir]}"

        # Loop through the URLs associated with the target directory
        for url in "${urls[@]}"; do
            # Extract the file name from the URL
            file_name=$(basename "$url")

            # Check if the file exists at the URL
            if curl --output /dev/null --silent --head --fail "$url"; then
                # Download the file and save it to the target directory
                curl -o "$target_dir/$file_name" "$url"
                echo "Downloaded $file_name to $target_dir"
            else
                echo "File does not exist at $url"
            fi
        done
    else
        echo "Target directory $target_dir does not exist. Skipping..."
    fi
done