# Gemini API Python Examples

This project contains examples of how to use the Google Gemini API with Python to perform various tasks such as generating text from images and text inputs, asking questions, and initiating chat sessions. The examples demonstrate how Python developers outside of GCP (not using Vertex AI) can use Gemini APIs when creating (and accounting) AI-generated content.

## Getting Started

To get started with these examples, you'll need to install the required dependencies listed in [requirements.txt](./requirements.txt):

```sh
pip install -r requirements.txt
```

Ensure you have a Google API key configured as an environment variable named GOOGLE_API_KEY to authenticate your requests to the Gemini API. You can create a key with one click in [Google AI Studio](https://aistudio.google.com/app/apikey).


## Examples

- [hi_gemini_omni.py](./hi_gemini_omni.py): Demonstrates how Gemini 1.5 models can handle multimodal inputs.
- [hi_gemini_chat.py](./hi_gemini_chat.py): Demonstrates chat conversations because they come with history support.
- [hi_gemini_ask.py](./hi_gemini_ask.py): Shows how to ask a question and receive an answer from the Gemini model.
- [gemini_models.py](./gemini_models.py): How to get the list of Gemini models.
- [hi_gemini.py](./hi_gemini.py): Check out how to count tokens in Gemini.

## Documentation

For more detailed information about the Google Gemini API and its capabilities, visit the [official documentation](https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python).
