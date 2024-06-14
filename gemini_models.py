"""
How to get the list of Gemini models from Google's Generative AI models.
"""
import pprint
import google.generativeai as genai

# https://ai.google.dev/api/python/google/generativeai/get_model
model = genai.get_model('models/gemini-pro')
pprint.pprint(model)

# https://ai.google.dev/api/python/google/generativeai/GenerativeModel
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"{m.name}: {m.description}")
