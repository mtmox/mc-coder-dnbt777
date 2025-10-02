
import os
import glob
import shutil
from aiqs import ModelInterface
from utils import create_version_folder, save_response, log_cost, get_user_instructions_from_nvim, read_mcignore, gather_files
from system_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv

# Load environment variables from the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(root_dir, '.env'))

def handle_get(llm_count, pattern, recursive, user_instructions=None):
    if user_instructions is None:
        user_instructions = get_user_instructions_from_nvim()

    version_folder = create_version_folder()
    backup_folder = os.path.join(version_folder, "backup")
    response_folder = os.path.join(version_folder, "responses")
    os.makedirs(backup_folder, exist_ok=True)
    os.makedirs(response_folder, exist_ok=True)

    files = gather_files(pattern, recursive)
    for file in files:
        backup_file_path = os.path.join(backup_folder, os.path.relpath(file, '.'))
        os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
        try:
            shutil.copy(file, backup_file_path)
        except PermissionError as e:
            print(f"PermissionError: {e}")
            continue

    prompt = SYSTEM_PROMPT + "\n"
    prompt += f'<user instructions>\n{user_instructions}\n</user instructions>\n'
    prompt += '<project files>\n'
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            prompt += f'<file path="{file}">{content}</file>\n'
        except UnicodeDecodeError as e:
            print(f"Error reading file {file}: {e}")
            print(f"Suggestion: Run 'mc ignore {file}' to ignore this file in future operations.")
            continue
    prompt += '</project files>'

    # Get model from environment variable, fallback to default
    model = os.getenv("AI_TOOLS_MODEL", "anthropic-sonnet-4")

    modelinterface = ModelInterface()
    for i in range(llm_count):
        response = modelinterface.send_to_ai(prompt, model=model, max_tokens=64*1000)
        response_text = response[0]  # Extract the actual response text from the tuple
        save_response(response_folder, i, response_text)
        if modelinterface.cost_tracker.cost_data:
            log_cost(modelinterface.cost_tracker.cost_data[-1])  # Log the latest cost data
            # Show cost data after each request
            print(f"\nCost data for request {i+1}:")
            modelinterface.cost_tracker.show_cost_data()
        else:
            print("No cost data available to log.")

    print(f"Responses saved in {response_folder}")

def handle_get_multifile(llm_count, file_names, user_instructions):
    """Handle multifile get command - similar to handle_get but works with specific file names"""
    version_folder = create_version_folder()
    backup_folder = os.path.join(version_folder, "backup")
    response_folder = os.path.join(version_folder, "responses")
    os.makedirs(backup_folder, exist_ok=True)
    os.makedirs(response_folder, exist_ok=True)

    # Backup the specified files
    valid_files = []
    for file_name in file_names:
        if os.path.isfile(file_name):
            valid_files.append(file_name)
            backup_file_path = os.path.join(backup_folder, os.path.relpath(file_name, '.'))
            os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
            try:
                shutil.copy(file_name, backup_file_path)
            except PermissionError as e:
                print(f"PermissionError: {e}")
                continue
        else:
            print(f"File not found: {file_name}")

    if not valid_files:
        print("No valid files found to process.")
        return

    # Build the prompt
    prompt = SYSTEM_PROMPT + "\n"
    prompt += f'<user instructions>\n{user_instructions}\n</user instructions>\n'
    prompt += '<project files>\n'

    for file_name in valid_files:
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read()
            prompt += f'<file path="{file_name}">{content}</file>\n'
        except UnicodeDecodeError as e:
            print(f"Error reading file {file_name}: {e}")
            continue

    prompt += '</project files>'

    # Get model from environment variable, fallback to default
    model = os.getenv("AI_TOOLS_MODEL", "anthropic-sonnet-4")

    # Send to AI
    modelinterface = ModelInterface()
    for i in range(llm_count):
        response = modelinterface.send_to_ai(prompt, model=model, max_tokens=64*1000)
        response_text = response[0]  # Extract the actual response text from the tuple
        save_response(response_folder, i, response_text)
        if modelinterface.cost_tracker.cost_data:
            log_cost(modelinterface.cost_tracker.cost_data[-1])  # Log the latest cost data
            # Show cost data after each request
            print(f"\nCost data for request {i+1}:")
            modelinterface.cost_tracker.show_cost_data()
        else:
            print("No cost data available to log.")

    print(f"Responses saved in {response_folder}")