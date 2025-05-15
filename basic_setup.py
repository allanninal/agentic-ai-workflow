"""
Basic OpenRouter API setup example

This script demonstrates how to properly set up the OpenRouter API client
using the OpenAI SDK with environment variables for API key management.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def setup_openrouter_client():
    """
    Initialize the OpenRouter client using the OpenAI SDK
    with proper configuration.
    
    Returns:
        OpenAI: Configured OpenAI client pointing to OpenRouter
    """
    # Get API key from environment variables
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        raise ValueError(
            "OpenRouter API key not found. Please set the OPENROUTER_API_KEY "
            "environment variable in your .env file."
        )
        
    # Initialize the client with OpenRouter configuration
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        # Optional headers for OpenRouter leaderboard
        default_headers={
            "HTTP-Referer": os.getenv("YOUR_SITE_URL", "http://localhost:5000"),
            "X-Title": os.getenv("YOUR_SITE_NAME", "Agentic AI Demo")
        }
    )
    
    return client

def test_connection():
    """Test the connection to OpenRouter API with a simple completion request."""
    try:
        client = setup_openrouter_client()
        
        # Make a simple test request
        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # OpenRouter model format
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, world!"}
            ],
        )
        
        print("✅ Successfully connected to OpenRouter API!")
        print(f"Model response: {completion.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ Error connecting to OpenRouter API: {e}")
        
if __name__ == "__main__":
    test_connection()