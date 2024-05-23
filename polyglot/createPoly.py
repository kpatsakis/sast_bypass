import os

def add_text_to_scripts(folder_path, prefix_text, suffix_text):
    # List all files in the specified folder
    script_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

    for script_file in script_files:
        input_script = os.path.join(folder_path, script_file)

        with open(input_script, 'r') as file:
            original_content = file.read()

        # Combine original content with prefix and suffix text
        modified_content = f"{prefix_text}{original_content}{suffix_text}"

        output_script = os.path.join(folder_path, f"modified_{script_file}")

        with open(output_script, 'w') as file:
            file.write(modified_content)

        print(f"Text added to {script_file} and saved as {output_script}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\asus\\Documents\\COSTAS_Code\\polyglot\\allScripts"  # Replace with the path to your folder containing Python scripts
    prefix_text = "#if 0 \nprint('Hello from Python!') \n#endif \n#if 0 \n\"\"\" \" \n#endif \n"
    suffix_text = "\n#if 0 \n\" \"\"\" \n#endif "

    add_text_to_scripts(folder_path, prefix_text, suffix_text)
