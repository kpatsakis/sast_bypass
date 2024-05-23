import json
import subprocess

# Specify the path to your JSONL file
file_path = "newdataset_alessandro.jsonl"

def run_snyk_test(input):
    try:
        # Run Snyk test command
        subprocess.run(["snyk", "code", "test", input], check=True)
        print("Snyk test completed successfully. No vulnerabilities found.")
    except subprocess.CalledProcessError as e:
        print(f"Snyk test failed with error:\n{e}")
        # You can handle the error or take appropriate actions based on your needs


with open(file_path, 'r') as jsonl_file:
    # Read each line and parse it as JSON
    i = 1
    for line in jsonl_file:
            python_script_file = str(i)+'_script.py'
            #print("Parsed JSON:", data)
            run_snyk_test(python_script_file)
            print(f"Python script '{python_script_file}' tested successfully.")
            
                