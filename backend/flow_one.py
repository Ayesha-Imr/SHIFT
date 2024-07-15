from langflow.load import run_flow_from_json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

def run_flow(url):
    TWEAKS = {
    "GroqModel-OXf40": {
        "groq_api_key": groq_api_key,
        "model_name": "llama3-70b-8192",
        "temperature": 0.1
    },
    "Prompt-EUZ9a": {
        "template": "You are an expert in sustainable shopping with a vast amount of knowledge on eco-friendliness and the impact of various products on the environment. Given the details about the product pasted below, your task is to do a detailed analysis on the environmental impact of the particular product on the environment. You are to do these things:\n1. Generate a short, generalised description of the product without mentioning any brand name or any specifics\n2. Rate the product's environment-friendliness on a scale from 0 (very harmful to the environment) to 10 (very good for the environment)\n3. Give a short summarised reason for your response in a single sentence\n4. Give a detailed reason for your response in a longer paragraph where you should mention in detail the reason for your rating and educate the user about the produt's environment impact, advice them on whether they should purchase the item or not, recycling options etc.\n\nGive your answer in the format of a python dictionary with the following keys: description, rating, summary, detail\nDo NOT include anything else in your response EXCEPT the python dictionary, no text, symbols or anything else. Do not forget to put both opening and closing curly brackets.\n\n{product}",
    },
    "ParseData-ExihH": {
        "sep": "\n",
        "template": "{value}"
    },
    "CustomComponent-oq3wJ": {
        "input_value": ""
    },
    "ParseData-CpuTA": {
        "sep": "\n",
        "template": "{value}"
    }
    }

    result = run_flow_from_json(
        flow="Product Eco-Friendliness Analysis.json",
        input_value=url,
        fallback_to_env_vars=True,
        tweaks=TWEAKS
    )

    print(result)

    # Extracting the chat response message
    if result:
        for output in result[0].outputs:
            message_data = output.results.get('message')
            if message_data:
                message_content = message_data.data.get('text', "")
                if message_content:
                    return message_content