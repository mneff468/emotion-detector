
"""Unit tests for the EmotionDetection package."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test emotion detection for five different emotions."""

    def test_joy(self):
        """Test that joyful text is classified as joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test that angry text is classified as anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test that disgusting text is classified as disgust."""
        result = emotion_detector(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Test that sad text is classified as sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Test that fearful text is classified as fear."""
        result = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
