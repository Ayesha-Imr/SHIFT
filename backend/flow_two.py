from langflow.load import run_flow_from_json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
search_api_key = os.getenv("SEARCH_API_KEY")

def get_alternatives(product_description):
    TWEAKS = {
    "GroqModel-3vsvr": {
        "groq_api_base": "",
        "groq_api_key": groq_api_key,
        "input_value": "",
        "model_name": "llama3-70b-8192",
        "system_message": "",
        "temperature": 0.1
    },
    "ToolCallingAgent-AYS28": {
        "handle_parsing_errors": True,
        "max_iterations": 15,
        "system_prompt": "You are a helpful assistant whose task is to search the internet for alternatives to the product whose description is given to you. The alternatives should be more environmental-friendly than this product and should have less negative impact on the climate. Do not write brand names in your search query not make it very narrow - be as general as possible in order to return a wide range of results. Clearly mention the product names and, if possible, brand names and purchase options so the user has the maximum amount of information and resources needed to purchase the item(s).",
        "user_prompt": "",
        "verbose": True
    },
    "SearchAPITool-XFHCW": {
        "api_key": search_api_key,
        "engine": "Google"
    },
    }

    print("product:  ", product_description)
    result = run_flow_from_json(flow="Sustainable Alternatives.json",
                                input_value=product_description,
                                fallback_to_env_vars=True, # False by default
                                tweaks=TWEAKS)
        
    print(result)
  
    # Extracting the specific text from the result
    extracted_text = ""  

    if result and len(result) > 0 and hasattr(result[0], 'outputs'):
        outputs = result[0].outputs
        if isinstance(outputs, list) and len(outputs) > 0:
            message_data = outputs[0].results.get('message')
            if message_data and hasattr(message_data, 'data'):
                extracted_text = message_data.data.get('text', "")
                print("Extracted Text: ", extracted_text)  # Print the extracted text

    return extracted_text



