# server.py
from flask import Flask, request, jsonify
import speech_recognition as sr
import io

app = Flask(__name__)

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    audio_file = request.files['audio']
    audio_data = io.BytesIO(audio_file.read())

    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return jsonify({'text': text})
    except sr.UnknownValueError:
        return jsonify({'error': 'Could not understand audio.'})
    except sr.RequestError as e:
        return jsonify({'error': f"Could not request results; {e}"})

if __name__ == '__main__':
    app.run(debug=True)
