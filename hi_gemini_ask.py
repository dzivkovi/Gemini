"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

LLM_MODEL = "gemini-1.5-flash"

model = genai.GenerativeModel(LLM_MODEL)

LLM_PROMPT = "What is the meaning of life?"

response = model.generate_content(
    LLM_PROMPT,
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        temperature=1,
        )
)

print(response.text)
