from sentiment import analyze_sentiment
from keywords import extract_keywords
from summarize import summarize_text

def full_pipeline(text):
    senti = analyze_sentiment(text)
    keys = extract_keywords(text)
    summ = summarize_text(text)
    return {"sentiment": senti, "keywords": keys, "summary": summ}
