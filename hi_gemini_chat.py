"""
See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
LLM_MODEL = "gemini-1.5-flash"

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name=LLM_MODEL,
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[]
)

INITIAL_PROMPT = "Hi there!"
response = chat_session.send_message(INITIAL_PROMPT)

print(f"""
Initial prompt
==============

{INITIAL_PROMPT}

Response
==============

{response.text}
""")
