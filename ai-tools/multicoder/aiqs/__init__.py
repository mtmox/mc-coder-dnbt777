
from aiqs.ModelInterface import ModelInterface
from dotenv import load_dotenv
import os

# Load environment variables from the ai-tools directory (parent of multicoder)
current_dir = os.path.dirname(os.path.abspath(__file__))
multicoder_dir = os.path.dirname(current_dir)  # Go up to multicoder
ai_tools_dir = os.path.dirname(multicoder_dir)  # Go up to ai-tools
env_path = os.path.join(ai_tools_dir, '.env')
load_dotenv(env_path)

# Now you can access the environment variables
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")