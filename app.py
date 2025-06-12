import gradio as gr
from src.sentiment import analyze_sentiment
from src.keywords import extract_keywords
from src.summarize import summarize_text

def analyze(text):
    senti = analyze_sentiment(text)
    keys = extract_keywords(text)
    summ = summarize_text(text)
    return senti, keys, summ

iface = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Türkçe Metin"),
    outputs=[
        gr.Textbox(label="Duygu Analizi"),
        gr.Textbox(label="Anahtar Kelimeler"),
        gr.Textbox(label="Özet")
    ],
    title="Türkçe Akıllı Metin Analiz Platformu"
)

if __name__ == "__main__":
    iface.launch()
