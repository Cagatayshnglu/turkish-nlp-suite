from transformers import pipeline

try:
    summarizer = pipeline('summarization', model='csebuetnlp/mT5_multilingual_XLSum')
except Exception:
    summarizer = None

def summarize_text(text):
    if summarizer is None:
        return "Model yüklenemedi."
    result = summarizer(text, min_length=15, max_length=60)
    return result[0]['summary_text']
