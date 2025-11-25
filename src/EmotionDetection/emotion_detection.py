import requests

WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
GET_REQ_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyse: str):
    GET_REQ_DATA = { "raw_document": { "text": text_to_analyse } }
    
    resp = requests.post(
        WATSON_URL,
        headers=GET_REQ_HEADERS,
        json=GET_REQ_DATA
    )

    emotions = resp.json().get('emotionPredictions', None)
    if emotions:
        emotions = emotions[0].get('emotion', None)

        # print(f"0 - emotions={emotions}")

        if emotions and type(emotions) is dict:
            emotions['dominant_emotion'] = max(emotions, key=emotions.get)
        else:
            print(f"Failed to get 'emotion'")
    else:
        print(f"Failed to get 'emotionPredictions'")

    if type(emotions) is not dict:
        emotions = {}

    # print(emotions)
    
    return emotions

def format_emotion_result(data: dict) -> str:
    dominant = data.get("dominant_emotion")
    # Preserve given order; exclude 'dominant_emotion'
    items = [(k, v) for k, v in data.items() if k != "dominant_emotion"]
    parts = [f"'{k}': {v}" for k, v in items]
    if not parts:
        body = "no emotions."
    elif len(parts) == 1:
        body = parts[0] + "."
    else:
        body = ", ".join(parts[:-1]) + " and " + parts[-1] + "."
    tail = f" The dominant emotion is {dominant}." if dominant else ""
    return f"For the given statement, the system response is {body}{tail}"