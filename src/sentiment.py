from transformers import pipeline

try:
    sentiment_model = pipeline('sentiment-analysis', model='savasy/bert-base-turkish-sentiment-cased')
except Exception:
    sentiment_model = None

def analyze_sentiment(text):
    if sentiment_model is None:
        return "Model yüklenemedi."
    result = sentiment_model(text)
    return f"{result[0]['label']} ({result[0]['score']:.2f})"
