from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    # Get the English text from the request body
    data = request.get_json()
    english_text = data.get('english_text', '')

    # Initialize the translator
    translator = Translator()

    # Translate the English text to Hindi
    hindi_text = translator.translate(english_text, dest='hi')

    # Create a response dictionary
    response = {
        'hindi': hindi_text.text,
        'hinglish': hindi_text.pronunciation
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
