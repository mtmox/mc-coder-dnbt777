#!/usr/bin/env python3

import sys
import os
import subprocess
import platform

# Add the multicoder directory to the path so we can import from it
current_dir = os.path.dirname(os.path.abspath(__file__))
multicoder_dir = os.path.join(current_dir, "multicoder")
sys.path.insert(0, multicoder_dir)

def copy_to_clipboard(text):
    """Copy text to clipboard using appropriate system command"""
    system = platform.system()
    
    try:
        if system == "Darwin":  # macOS
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            process.communicate(text.encode('utf-8'))
        elif system == "Linux":
            # Try xclip first, then xsel as fallback
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(text.encode('utf-8'))
            except FileNotFoundError:
                try:
                    process = subprocess.Popen(['xsel', '--clipboard', '--input'], stdin=subprocess.PIPE)
                    process.communicate(text.encode('utf-8'))
                except FileNotFoundError:
                    print("Error: No clipboard utility found. Please install xclip or xsel.")
                    return False
        elif system == "Windows":
            process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
            process.communicate(text.encode('utf-8'))
        else:
            print(f"Error: Unsupported operating system: {system}")
            return False
        
        return True
    except Exception as e:
        print(f"Error copying to clipboard: {e}")
        return False

def get_multifile_prompt(file_names):
    """Generate multifile prompt from list of file names"""
    s = ""
    
    for file_name in file_names:
        if os.path.isfile(file_name):
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    file_contents = f.read()
                
                # Append the formatted string to s
                s += f"```{file_name}\n{file_contents}```\n"
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
        else:
            print(f"File not found: {file_name}")
    
    return s

def handle_multifile_get(file_names):
    """Handle the gmfp 1 command by calling multicoder's get functionality"""
    try:
        from get import handle_get_multifile
        from utils import get_user_instructions_from_nvim
        
        # Get user instructions using nvim (same as mc get)
        user_instructions = get_user_instructions_from_nvim()
        
        # Call the multifile version of handle_get
        handle_get_multifile(1, file_names, user_instructions)
        
    except ImportError as e:
        print(f"Error importing multicoder modules: {e}")
        print("Falling back to clipboard copy...")
        # Fallback to original behavior
        prompt_text = get_multifile_prompt(file_names)
        if prompt_text:
            if copy_to_clipboard(prompt_text):
                print(f"Multifile prompt for {len(file_names)} files copied to clipboard.")
            else:
                print("Failed to copy to clipboard. Here's the content:")
                print(prompt_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: gmfp <file1> <file2> ... <fileN>")
        print("       gmfp 1 \"file1\" \"file2\" \"file3\"")
        sys.exit(1)
    
    # Check if first argument is "1" (compatibility with mc get 1 format)
    if sys.argv[1] == "1":
        # Handle format: gmfp 1 "file1" "file2" "file3" (each file in separate quotes)
        file_names = sys.argv[2:]
        # Use multicoder functionality
        handle_multifile_get(file_names)
    else:
        # Handle format: gmfp filename1.py filename2.sh filename3.go
        file_names = sys.argv[1:]
        # Generate the multifile prompt and copy to clipboard (original behavior)
        prompt_text = get_multifile_prompt(file_names)
        
        if prompt_text:
            # Copy to clipboard
            if copy_to_clipboard(prompt_text):
                print(f"Multifile prompt for {len(file_names)} files copied to clipboard.")
            else:
                print("Failed to copy to clipboard. Here's the content:")
                print(prompt_text)
        else:
            print("No valid files found or processed.")

if __name__ == "__main__":
    main()
