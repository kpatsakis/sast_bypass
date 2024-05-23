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

try:
    with open(file_path, 'r') as jsonl_file:
        # Read each line and parse it as JSON
        i = 1
        for line in jsonl_file:
            try:
                data = json.loads(line)
                #print("Parsed JSON:", data)
                #run_snyk_test(data)
                # Specify the output Python script file
                python_script_file = str(i)+'_script.pyc'

                # Write the Python script containing the JSON data
                with open(python_script_file, 'w') as script_file:
                    #print(json.dumps(data, indent=2))
                    intermediate = json.dumps(data)
                    script_file.write(intermediate[1:-1])

                print(f"Python script '{python_script_file}' generated successfully.")
                i = i+ 1

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


