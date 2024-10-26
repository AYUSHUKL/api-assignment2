from transformers import pipeline

def answer_question(question, context):
    qa_pipeline = pipeline("question-answering")
    return qa_pipeline(question=question, context=context)
