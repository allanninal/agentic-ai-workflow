"""
OpenRouter Model Comparison Example

This script demonstrates how to access models from different providers
(OpenAI, Anthropic, Google, etc.) using OpenRouter's unified API.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenRouter client
def get_client():
    """
    Initialize and return the OpenRouter client
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": os.getenv("YOUR_SITE_URL", "http://localhost:5000"),
            "X-Title": os.getenv("YOUR_SITE_NAME", "Model Comparison Demo")
        }
    )
    
    return client

def generate_response(model, prompt):
    """
    Generate a response using the specified model
    
    Args:
        model (str): OpenRouter model identifier
        prompt (str): Text prompt to send to the model
        
    Returns:
        str: The model's response
    """
    client = get_client()
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def compare_models(prompt):
    """
    Compare responses from different models for the same prompt
    
    Args:
        prompt (str): The prompt to send to all models
    """
    # Define models from different providers to test
    models = {
        "OpenAI GPT-3.5": "openai/gpt-3.5-turbo",
        "OpenAI GPT-4": "openai/gpt-4",
        "Anthropic Claude": "anthropic/claude-instant-1",
        "Google PaLM 2": "google/palm-2-chat-bison", 
        "Mistral": "mistralai/mistral-7b-instruct-v0.2"
    }
    
    print(f"Prompt: {prompt}\n")
    print("-" * 50)
    
    for name, model_id in models.items():
        try:
            print(f"\n{name} ({model_id}):")
            response = generate_response(model_id, prompt)
            print(f"Response: {response}\n")
            print("-" * 50)
        except Exception as e:
            print(f"Error with {name}: {str(e)}")
            print("-" * 50)

if __name__ == "__main__":
    # Example prompt for comparison
    test_prompt = "Explain quantum computing in simple terms."
    
    compare_models(test_prompt) 