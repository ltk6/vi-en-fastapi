from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from translation import translate_text

class TextRequest(BaseModel):
    text: str

app = FastAPI(
    title="Vietnamese to English Translation API",
    description="Translate text from Vietnamese to English",
    version="1.0"
)

@app.get("/")
def root():
    return {
        "message": "Translation API using Hugging Face",
        "endpoint": "/predict"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: TextRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        result = translate_text(text)
        return {
            "input": text,
            "translation": result
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Translation failed")