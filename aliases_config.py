
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

easy_modular_scripts_dir = current_dir

aliases = {
    # ask-app
    "ask": f"python3 {current_dir}/ask-app/ask.py",
    "runit": f"bash {current_dir}/ask-app/runit.sh",

    # ai tools
    "gmfp": f"python3 {current_dir}/ai-tools/get_multifile_prompt.py", # get multifile prompt
    "mkfiles":f"python3 {current_dir}/ai-tools/make_multifile.py", # takes clipboard and makes the multifile project
    "mcoder":f"python3 {current_dir}/ai-tools/multicoder/multicoder.py",
    "mc":"mcoder",
    
    # meta stuff
    "update-aliases":f"python3 {current_dir}/update-all.py;exec bash",
    "emsupdate":f"update-aliases",

    # Add more aliases as needed
    # "alias_name": "command",
}
