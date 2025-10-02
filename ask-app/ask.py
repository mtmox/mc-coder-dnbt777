
import os
import sys
from dotenv import load_dotenv

# Add the multicoder directory to the path so we can import aiqs
multicoder_dir = os.path.join(os.path.dirname(__file__), '..', 'ai-tools', 'multicoder')
sys.path.insert(0, multicoder_dir)

from aiqs import ModelInterface

def main():
    # Load environment variables from root .env
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(root_dir, '.env'))

    # Get the model to use from environment variable, default to OpenRouter OpenAI GPT-4o
    model = os.getenv('ASK_APP_MODEL')

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get command line arguments (excluding the script name)
    args = sys.argv[1:]

    if not args:
        print("Usage: python ask.py <prompt>")
        sys.exit(1)

    # Combine the system prompt with the user prompt
    system_prompt = "Answer in as few characters as possible. No formatting tokens such as ` or ```"
    user_prompt = ' '.join(args)

    try:
        # Initialize the model interface for OpenRouter
        modelinterface = ModelInterface()
        
        # Send the request to the AI
        response = modelinterface.send_to_ai(
            prompt=user_prompt,
            model=model,
            max_tokens=300,
            temperature=0.7,
            system_prompt=system_prompt
        )
        
        # Extract and print the response
        response_text = response[0] if isinstance(response, tuple) else response
        print(response_text)

        # Save the response to the last_output.log file in the ask_app_dir
        ask_app_dir = os.getenv('EasyModularScriptsDir', '') + "/ask-app/"
        if ask_app_dir:
            log_file_path = os.path.join(ask_app_dir, 'last_output.log')
            with open(log_file_path, 'w') as log_file:
                log_file.write(response_text)
        else:
            print("Error: The EasyModularScriptsDir environment variable is not set.")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
