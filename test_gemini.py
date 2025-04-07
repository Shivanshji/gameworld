import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('GEMINI_API_KEY')
print(f"API key found: {'Yes' if api_key else 'No'}")

# Configure genai
genai.configure(api_key=api_key)

# List available models
print("\nAvailable models:")
for m in genai.list_models():
    print(m.name)

# Try to create model
try:
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content("Hello, test message")
    print("\nTest response:", response.text)
except Exception as e:
    print("\nError:", str(e)) 