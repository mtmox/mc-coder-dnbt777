
import os
from aiqs.model_list import openrouter_models

def handle_model():
    # Ask which model to change
    print("Which model would you like to change?")
    print("1. AI_TOOLS_MODEL")
    print("2. ASK_APP_MODEL")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        env_var = "AI_TOOLS_MODEL"
    elif choice == "2":
        env_var = "ASK_APP_MODEL"
    else:
        print("Invalid choice.")
        return
    
    # Display available models
    print(f"\nAvailable models for {env_var}:")
    for i, model in enumerate(openrouter_models, 1):
        print(f"{i}. {model}")
    
    # Ask user to pick a model
    try:
        model_index = int(input("Enter the number of the model you want to use: ").strip()) - 1
        if 0 <= model_index < len(openrouter_models):
            selected_model = openrouter_models[model_index]
        else:
            print("Invalid model number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Update the .env file
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    env_path = os.path.join(root_dir, '.env')
    
    # Read the current .env content
    if os.path.exists(env_path):
        with open(env_path, 'r') as file:
            lines = file.readlines()
    else:
        lines = []
    
    # Check if the env_var is already in the file
    updated = False
    for i, line in enumerate(lines):
        if line.startswith(f"{env_var}="):
            lines[i] = f"{env_var}={selected_model}\n"
            updated = True
            break
    
    # If not found, add it
    if not updated:
        lines.append(f"{env_var}={selected_model}\n")
    
    # Write back to .env
    with open(env_path, 'w') as file:
        file.writelines(lines)
    
    print(f"Updated {env_var} to {selected_model} in {env_path}")
