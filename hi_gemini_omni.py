"""
Generate text from image and text inputs
https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python
"""

import os
import PIL.Image
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

LLM_MODEL = "gemini-1.5-flash"

model = genai.GenerativeModel(LLM_MODEL)

img = PIL.Image.open('cookie.png')
LLM_PROMPT = "Do these look store-bought or homemade?"
response = model.generate_content([LLM_PROMPT, img], stream=True)
response.resolve()

print(response.text)
