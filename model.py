import google.generativeai as genai
import os
# Replace with your actual Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all available models
models = genai.list_models()

# Display models and supported methods
for m in models:
    print(f"Model Name: {m.name}")
    print(f"Supports generateContent: {'generateContent' in m.supported_generation_methods}")
    print("-" * 50)
