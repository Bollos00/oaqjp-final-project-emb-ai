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
        return "Invalid text! Please try again!", 400

    resp = emotion_detector(text)

    if not resp.get("dominant_emotion", None):
        return "Invalid text! Please try again!", 500

    return format_emotion_result(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
