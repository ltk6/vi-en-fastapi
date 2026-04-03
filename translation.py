from transformers import pipeline

model = pipeline("translation", model="Helsinki-NLP/opus-mt-vi-en")

def translate_text(text: str):
    try:
        output = model(text)
        return output[0]["translation_text"]
    except Exception:
        raise