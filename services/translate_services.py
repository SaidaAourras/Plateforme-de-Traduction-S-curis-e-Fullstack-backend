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

def translate_text(choice:str , text:str):
    user_text = text
    if (choice == 'en-fr'):
        return english_to_frensh(user_text)
    elif (choice == 'fr-en'):
        return frensh_to_english(user_text)
    else:
        return {'warning':'out of choices en-fr , fr-en'}

