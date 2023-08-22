#!/bin/bash

# Create an array to store the list of files
file_list=()

# Loop through files in the current directory and add those starting with "out" to the array
for file in ./output*; do
    if [ -f "$file" ]; then
        file_list+=("$file")
    fi
done
echo "${file_list[@]}"
python chartcreate.py "${file_list[@]}"
