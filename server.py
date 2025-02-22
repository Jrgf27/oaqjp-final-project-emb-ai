"""Module providing Flask functions"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask('EmotionAnalyser')

@app.route('/emotionDetector')
def emotion_route():
    "Function for GET method on emotion check"
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return 'Invalid input! Try again'
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    "Function for GET method on index page"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    