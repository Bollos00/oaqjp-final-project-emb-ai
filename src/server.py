"""Flask application entrypoint for the emotion detection web service.

Exposes a simple index page and a GET endpoint that proxies text to the
emotion detection logic and returns a formatted result string.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector, format_emotion_result

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.get("/")
def index():
    """Render the index page with the UI for text input."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Handle emotion detection requests via query param `textToAnalyze`.

    Returns a human-readable string or an error message with appropriate
    HTTP status codes when input is missing or the detector fails.
    """
    text = request.args.get("textToAnalyze")
    if not text:
        return "Invalid text! Please try again!", 400

    resp = emotion_detector(text)

    if not resp.get("dominant_emotion", None):
        return "Invalid text! Please try again!", 500

    return format_emotion_result(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
