from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="t5-small")
    return summarizer(text, max_length=50, min_length=25, do_sample=False)
