from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result = {
        "anger": response["anger"],
        "disgust": response["disgust"],
        "fear": response["fear"],
        "joy": response["joy"],
        "sadness": response["sadness"],
        "dominant_emotion": response["dominant_emotion"]
    }

    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

