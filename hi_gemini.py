"""
Demonstrates how to count tokens in a Gemini prompt and response. Borrowed from the Vertex AI Python SDK:
https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count
"""
import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Define the model to use
LLM_MODEL = "gemini-1.5-flash"

# Create the model object
model = genai.GenerativeModel(LLM_MODEL)

# Define the prompt
prompt = "Generate a trivia question and an answer"

# FYI: Prompt tokens count
response = model.count_tokens(prompt)
print(f"Prompt Token Count: {response.total_tokens}")

# Generate the content
response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        candidate_count=1,
        temperature=1,
    )
)

# Print the response
query_response = response.text if response.text else "No response"
llm_model = response.model_id if hasattr(response, 'model_id') else LLM_MODEL

print(f"Response: {query_response}")
print(f"Model: {llm_model}")

# Use to get both input and output token counts
usage_metadata = response.usage_metadata
print(f"Prompt Token Count: {usage_metadata.prompt_token_count}")
print(f"Candidates Token Count: {usage_metadata.candidates_token_count}")
print(f"Total Token Count: {usage_metadata.total_token_count}")
