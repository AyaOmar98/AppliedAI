# server.py
from flask import Flask, request, jsonify
from translator.translator import TranslationService

app = Flask(__name__)

# Create an instance of the TranslationService
translator_service = TranslationService()

@app.route('/')
def index():
    return "Welcome to the Translation Service!"

@app.route('/translate/french_to_english', methods=['POST'])
def french_to_english():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text')
        translated_text = translator_service.french_to_english(text)
        return jsonify({'translated_text': translated_text})

@app.route('/translate/english_to_french', methods=['POST'])
def english_to_french():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text')
        translated_text = translator_service.english_to_french(text)
        return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run()
