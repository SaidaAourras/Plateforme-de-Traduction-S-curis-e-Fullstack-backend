import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def frensh_to_english(text):
    client = InferenceClient(
        provider="hf-inference",
        api_key=os.getenv("HF_TOKEN"),
    )

    result = client.translation(
        text,
        model="Helsinki-NLP/opus-mt-fr-en",
    )

    return result

# print(frensh_to_english('bonjour'))
