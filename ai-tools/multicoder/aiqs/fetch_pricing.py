
import requests
import re
import math
import importlib.util
import sys
from typing import Dict, Any, List

def load_target_models_from_py(file_path: str = "model_list.py") -> List[str]:
    """Load the list of models from model_list.py file."""
    spec = importlib.util.spec_from_file_location("model_list", file_path)
    model_list_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model_list_module)
    
    return model_list_module.openrouter_models

def query_openrouter_models() -> Dict[str, Any]:
    """Query OpenRouter API to get all available models and their information."""
    url = "https://openrouter.ai/api/v1/models"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error querying OpenRouter API: {e}")
        return {}

def round_up_price(price: float, decimal_places: int = 6) -> float:
    """Round up a price to avoid long decimal representations."""
    if price == 0:
        return 0.0
    
    # Use ceiling to always round up
    multiplier = 10 ** decimal_places
    return math.ceil(price * multiplier) / multiplier

def extract_pricing_info(api_response: Dict[str, Any], target_models: List[str]) -> Dict[str, Dict[str, float]]:
    """Extract pricing information for our target models from the API response."""
    pricing_info = {}
    
    if 'data' not in api_response:
        print("No 'data' field found in API response")
        return pricing_info
    
    # Create a mapping of model IDs from the API
    api_models = {model['id']: model for model in api_response['data']}
    
    for target_model in target_models:
        # Try exact match first
        if target_model in api_models:
            model_data = api_models[target_model]
            pricing = model_data.get('pricing', {})
            
            # Convert pricing to our format (per 1 million tokens) and round up
            if pricing:
                # Multiply by 1000 twice: once to get per 1000 tokens, then again to get per 1 million tokens
                input_price = float(pricing.get('prompt', 0)) * 1000 * 1000
                output_price = float(pricing.get('completion', 0)) * 1000 * 1000
                
                pricing_info[target_model] = {
                    "input": round_up_price(input_price),
                    "output": round_up_price(output_price)
                }
                
                # Add additional pricing fields if they exist
                if pricing.get('image'):
                    pricing_info[target_model]["image"] = round_up_price(float(pricing['image']))
                if pricing.get('request'):
                    pricing_info[target_model]["request"] = round_up_price(float(pricing['request']))
                    
                print(f"Found pricing for {target_model}")
            else:
                print(f"No pricing information found for {target_model}")
        else:
            # Try to find similar models (in case of slight naming differences)
            similar_models = [model_id for model_id in api_models.keys() 
                            if target_model.lower() in model_id.lower() or 
                               model_id.lower() in target_model.lower()]
            
            if similar_models:
                print(f"Model {target_model} not found exactly, but found similar: {similar_models}")
                # You might want to manually map these or ask for user input
            else:
                print(f"Model {target_model} not found in OpenRouter API")
    
    return pricing_info

def update_model_list_file(pricing_info: Dict[str, Dict[str, float]], file_path: str = "model_list.py"):
    """Update the model_list.py file with the new pricing information."""
    
    # Read the current file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Build the new model_pricing dictionary string
    pricing_dict_str = "model_pricing = {\n"
    
    for model_id, pricing in pricing_info.items():
        pricing_dict_str += f'    "{model_id}": {{\n'
        pricing_dict_str += f'        "input": {pricing["input"]},  # per 1 million tokens\n'
        pricing_dict_str += f'        "output": {pricing["output"]},   # per 1 million tokens\n'
        
        # Add additional pricing fields if they exist
        if "image" in pricing:
            pricing_dict_str += f'        "image": {pricing["image"]},  # per image\n'
        if "request" in pricing:
            pricing_dict_str += f'        "request": {pricing["request"]},  # per request\n'
            
        pricing_dict_str += "    },\n"
    
    pricing_dict_str += "}"
    
    # Find the start and end of the model_pricing dictionary
    # Look for the pattern "model_pricing = {" and find the matching closing brace
    start_pattern = r'model_pricing\s*=\s*\{'
    start_match = re.search(start_pattern, content)
    
    if start_match:
        start_pos = start_match.start()
        
        # Find the matching closing brace by counting braces
        brace_count = 0
        pos = start_match.end() - 1  # Start from the opening brace
        
        while pos < len(content):
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_pos = pos + 1
                    break
            pos += 1
        else:
            # If we couldn't find the matching brace, fall back to simple replacement
            print("Warning: Could not find matching closing brace, using simple replacement")
            pattern = r'model_pricing\s*=\s*\{[^}]*\}'
            updated_content = re.sub(pattern, pricing_dict_str, content, flags=re.DOTALL)
        
        if 'end_pos' in locals():
            # Replace the entire model_pricing dictionary
            updated_content = content[:start_pos] + pricing_dict_str + content[end_pos:]
        else:
            updated_content = content
    else:
        # If no existing model_pricing found, append it
        updated_content = content + f"\n\n# Updated pricing information\n{pricing_dict_str}\n"
    
    # Write the updated content back to the file
    with open(file_path, 'w') as f:
        f.write(updated_content)
    
    print(f"Updated {file_path} with pricing information for {len(pricing_info)} models")

def main():
    """Main function to orchestrate the pricing update process."""
    print("Loading target models from model_list.py...")
    target_models = load_target_models_from_py()
    
    print(f"Loaded {len(target_models)} target models")
    print("Querying OpenRouter API...")
    
    api_response = query_openrouter_models()
    
    if not api_response:
        print("Failed to get API response")
        return
    
    print(f"API returned {len(api_response.get('data', []))} models")
    print("Extracting pricing information...")
    
    pricing_info = extract_pricing_info(api_response, target_models)
    
    if pricing_info:
        print(f"Found pricing for {len(pricing_info)} models")
        print("Updating model_list.py...")
        update_model_list_file(pricing_info)
        print("Pricing update complete!")
    else:
        print("No pricing information found for any target models")

if __name__ == "__main__":
    main()
