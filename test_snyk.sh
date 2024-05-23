#!/bin/bash

# Specify the directory containing the files to be processed
input_directory="C:\Users\asus\Documents\COSTAS_code"

# Iterate over each file in the input directory
for file in "$input_directory"/*
do
    # Check if the item is a file (not a directory)
    if [ -f "$file" ]; then
        # Extract the file name without extension
        filename=$(basename -- "$file")
        filename_noext="${filename%.*}"

        # Execute your command for each file and save output to a text file
        snyk code test "$filename" > "${filename_noext}_output.txt"

        # Optionally, display a message indicating completion for each file
        echo "Processed $file. Output saved to ${filename_noext}_output.txt"
    fi
done

# Optionally, display a message indicating completion of the script
echo "Script completed."
