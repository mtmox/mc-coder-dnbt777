import os
import sys
import importlib

def print_directory_structure(start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

# Print current working directory and Python path
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Add the parent directory of the script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

print(f"Updated Python path: {sys.path}")

# Print the directory structure
print("\nDirectory structure:")
print_directory_structure(parent_dir)

# Try to import the module and print detailed information
try:
    print("\nAttempting to import aiqs.ModelInterface...")
    aiqs = importlib.import_module('aiqs')
    print(f"Successfully imported aiqs package. Location: {aiqs.__file__}")
    
    ModelInterface = importlib.import_module('aiqs.ModelInterface')
    print(f"Successfully imported ModelInterface. Location: {ModelInterface.__file__}")
    
    from aiqs.ModelInterface import ModelInterface
    print("Successfully imported ModelInterface class")
except ImportError as e:
    print(f"Import error: {e}")
    print("Attempting to import individual components...")
    try:
        import boto3
        print("boto3 is installed and imported successfully")
    except ImportError:
        print("boto3 is not installed. Please install it using: pip install boto3")
    
    try:
        from aiqs.ModelInterface import ModelInterface
        print("Successfully imported ModelInterface class")
    except ImportError as e:
        print(f"Failed to import ModelInterface: {e}")
        ModelInterface = None

from dotenv import load_dotenv

def run_unit_tests():
    load_dotenv()
    if ModelInterface is None:
        print("ModelInterface could not be imported. Cannot run tests.")
        return
    
    model_interface = ModelInterface()
    models = [
        "anthropic-opus",
        "anthropic-sonnet3.5",
    ]
    test_prompt = "Say your name, then the capital of France, then a prime number"
    print("Running unit tests for each model:")
    for model in models:
        print(f"\nTesting {model}:")
        try:
            response, metrics = model_interface.send_to_ai(test_prompt, model, max_tokens=50)
            print(f"Response: {response.strip()}")
            print(f"Metrics: {metrics}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_unit_tests()