import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def english_to_frensh(text):
    client = InferenceClient(
        provider="hf-inference",
        api_key=os.getenv("HF_TOKEN"),
    )

    result = client.translation(
        text,
        model="Helsinki-NLP/opus-mt-en-fr",
    )

    return result
