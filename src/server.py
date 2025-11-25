from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector, format_emotion_result

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotionDetector():
    text = request.args.get("textToAnalyze")
    if not text:
        return "Missing 'textToAnalyze'", 400

    resp = format_emotion_result(emotion_detector(text))

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
