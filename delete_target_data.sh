#!/bin/bash
# Script to clear the current target data including database, logfile and all media files

# List of files and directories to be deleted
items=("instamon.log" "target.db" "target/")

# Loop through and delete each item
for item in "${items[@]}"; do
    if [ -e "$item" ]; then
        echo "Deleting: $item"
        rm -r "$item"
    else
        echo "Not found: $item"
    fi
done

echo "Deletion complete."
