# list_models.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your .env file if you're using one
load_dotenv()

# Configure with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all models
models = genai.list_models()

print("✅ Available Gemini models:")
for model in models:
    methods = model.supported_generation_methods
    print(f"- {model.name} | supports: {methods}")
