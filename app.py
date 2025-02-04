from flask import Flask, render_template, request
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

def load_model(src_lang, tgt_lang):
    """Loads the MarianMT model for translation."""
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Load models for translation
tokenizer_sa_en, model_sa_en = load_model("sa", "en")  # Sanskrit → English
tokenizer_en_hi, model_en_hi = load_model("en", "hi")  # English → Hindi

def translate_text(text, tokenizer, model):
    """Translates input text using the specified model and tokenizer."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

@app.route("/", methods=["GET", "POST"])
def index():
    translation_result = ""
    
    if request.method == "POST":
        text = request.form["text"]
        translation_type = request.form["translation_type"]

        if translation_type == "sa-en":
            translation_result = translate_text(text, tokenizer_sa_en, model_sa_en)
        elif translation_type == "en-hi":
            translation_result = translate_text(text, tokenizer_en_hi, model_en_hi)
    
    return render_template("index.html", translation_result=translation_result)

if __name__ == "__main__":
    app.run(debug=True)
    