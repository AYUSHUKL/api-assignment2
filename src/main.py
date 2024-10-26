from fastapi import FastAPI, UploadFile, File
from src.nlp.summarizer import summarize_text
from src.nlp.sentiment_analysis import analyze_sentiment
from src.nlp.question_answering import answer_question
from src.cv.image_classifier import classify_image
from src.cv.ocr import extract_text_from_image

app = FastAPI()

@app.post("/summarize/")
async def summarize(text: str):
    return {"summary": summarize_text(text)}

@app.post("/sentiment/")
async def sentiment(text: str):
    return {"sentiment": analyze_sentiment(text)}

@app.post("/qa/")
async def qa(question: str, context: str):
    return {"answer": answer_question(question, context)}

@app.post("/classify-image/")
async def classify_image(file: UploadFile = File(...)):
    return {"classification": classify_image(file)}

@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    return {"text": extract_text_from_image(file)}
