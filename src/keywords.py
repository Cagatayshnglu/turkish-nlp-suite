from keybert import KeyBERT

try:
    kw_model = KeyBERT(model='distilbert-base-turkish-cased')
except Exception:
    kw_model = None

def extract_keywords(text, n=5):
    if kw_model is None:
        return "Model yüklenemedi."
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words=None)
    return ', '.join([kw[0] for kw in keywords[:n]])
