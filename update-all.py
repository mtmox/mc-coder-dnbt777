import os
from aliases_config import aliases, easy_modular_scripts_dir

def add_or_update_alias_in_zshrc(alias_name, command):
    zshrc_path = os.path.expanduser("~/.zshrc")
    alias_line = f"alias {alias_name}='{command}'\n"
    
    # Read the current .zshrc content
    if os.path.exists(zshrc_path):
        with open(zshrc_path, 'r') as file:
            lines = file.readlines()
    else:
        lines = []
    
    # Remove any existing lines that define the alias
    lines = [line for line in lines if not line.startswith(f"alias {alias_name}=")]
    
    # Add the new alias line
    lines.append(alias_line)
    print(f"Alias '{alias_name}' added or updated in .zshrc.")
    
    # Write the updated lines back to the .zshrc file
    with open(zshrc_path, 'w') as file:
        file.writelines(lines)

def add_current_dir_to_zshrc():
    zshrc_path = os.path.expanduser("~/.zshrc")
    env_var_line = f"export EasyModularScriptsDir='{easy_modular_scripts_dir}'\n"
    
    # Read the current .zshrc content
    if os.path.exists(zshrc_path):
        with open(zshrc_path, 'r') as file:
            lines = file.readlines()
    else:
        lines = []
    
    # Remove any existing lines that define the environment variable
    lines = [line for line in lines if not line.startswith("export EasyModularScriptsDir=")]
    
    # Add the new environment variable line
    lines.append(env_var_line)
    print(f"Environment variable 'EasyModularScriptsDir' added or updated in .zshrc.")
    
    # Write the updated lines back to the .zshrc file
    with open(zshrc_path, 'w') as file:
        file.writelines(lines)

def update_env_files_with_current_dir():
    current_dir = os.getcwd()
    env_var_line = f"EasyModularScriptsDir='{current_dir}'\n"
    
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file == ".env":
                env_path = os.path.join(root, file)
                
                # Read the current .env content
                if os.path.exists(env_path):
                    with open(env_path, 'r') as file:
                        lines = file.readlines()
                else:
                    lines = []
                
                # Remove any existing lines that define the environment variable
                lines = [line for line in lines if not line.startswith("EasyModularScriptsDir=")]
                
                # Add the new environment variable line
                lines.append(env_var_line)
                print(f"Environment variable 'EasyModularScriptsDir' added or updated in {env_path}.")
                
                # Write the updated lines back to the .env file
                with open(env_path, 'w') as file:
                    file.writelines(lines)

def main():
    for alias_name, command in aliases.items():
        add_or_update_alias_in_zshrc(alias_name, command)
        add_current_dir_to_zshrc()
        update_env_files_with_current_dir()
        # Reload the .zshrc file to apply changes
    print("Please run 'source ~/.zshrc' or start a new terminal session to apply changes.")

if __name__ == "__main__":
    main()