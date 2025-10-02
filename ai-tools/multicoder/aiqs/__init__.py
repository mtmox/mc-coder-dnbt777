
from aiqs.ModelInterface import ModelInterface
from dotenv import load_dotenv
import os

# Load environment variables from the root directory
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
load_dotenv(os.path.join(root_dir, '.env'))

# Now you can access the environment variables
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
