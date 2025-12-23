"""
High-level sentiment analysis logic.
"""

import logging
from collections import Counter
from typing import Dict, List

from sentiment_analyzer.model import SentimentModel
from sentiment_analyzer.preprocessing import clean_text

logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    """
    Combines preprocessing and ML model
    to perform sentiment analysis.
    """

    def __init__(self) -> None:
        self.model = SentimentModel()
        self._train_default_model()

    def _train_default_model(self) -> None:
        """
        Train the model on a small demo dataset.
        """
        texts = [
            "I love this product",
            "This is amazing",
            "I hate this",
            "This is terrible",
            "It is okay",
        ]
        labels = ["positive", "positive", "negative", "negative", "neutral"]
        cleaned_texts = [clean_text(text) for text in texts]

        self.model.train(cleaned_texts, labels)
        logger.info("Default sentiment model trained")

    def analyze(self, texts: List[str]) -> List[Dict[str, float | str]]:
        """
        Analyze sentiment for a list of texts.
        """
        cleaned_texts = [clean_text(text) for text in texts]
        predictions = self.model.predict_with_confidence(cleaned_texts)

        return [
            {"sentiment": sentiment, "confidence": round(confidence, 3)}
            for sentiment, confidence in predictions
        ]

    def statistics(self, results: List[Dict[str, float | str]]) -> Dict[str, int]:
        """
        Calculate sentiment distribution.
        """
        sentiments = [result["sentiment"] for result in results]
        return dict(Counter(sentiments))
