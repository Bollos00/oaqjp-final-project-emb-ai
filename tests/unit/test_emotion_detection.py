import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection_joy(self):
        result = emotion_detector("I am glad this happened").get("dominant_emotion", "")
        self.assertEqual(result, "joy")

    def test_emotion_detection_anger(self):
        result = emotion_detector("I am really mad about this").get("dominant_emotion", "")
        self.assertEqual(result, "anger")

    def test_emotion_detection_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this").get("dominant_emotion", "")
        self.assertEqual(result, "disgust")

    def test_emotion_detection_sadness(self):
        result = emotion_detector("I am so sad about this").get("dominant_emotion", "")
        self.assertEqual(result, "sadness")

    def test_emotion_detection_fear(self):
        result = emotion_detector("I am really afraid that this will happen").get("dominant_emotion", "")
        self.assertEqual(result, "fear")
