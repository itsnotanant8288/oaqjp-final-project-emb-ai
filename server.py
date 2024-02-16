"""
This module implements a Flask-based web application for emotion analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the text passed as a query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid input ! Try again."
    formatted_response = "For the given statement, the system response is "
    for emotion, value in response.items():
        if emotion != "dominant_emotion":
            formatted_response += f"'{emotion}': {value}, "
    formatted_response = formatted_response[:-2]  # Removing the trailing comma and space
    formatted_response += f". The dominant emotion is {response['dominant_emotion']}."
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Renders the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
