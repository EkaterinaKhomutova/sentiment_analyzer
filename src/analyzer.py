import logging
from typing import Dict, List
from collections import Counter

from src.preprocessing import clean_text
from src.model import SentimentModel

logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    """
    Sentiment analysis logic.
    """

    def __init__(self) -> None:
        self.model = SentimentModel()
        self._train_default_model()

    def _train_default_model(self) -> None:
        texts = [
            "I love this product",
            "This is amazing",
            "I hate this",
            "This is terrible",
            "It is okay",
        ]
        labels = ["positive", "positive", "negative", "negative", "neutral"]
        cleaned = [clean_text(t) for t in texts]
        self.model.train(cleaned, labels)
        logger.info("Default sentiment model trained")

    def analyze(self, texts: List[str]) -> List[Dict[str, float | str]]:
        cleaned = [clean_text(t) for t in texts]
        predictions = self.model.predict_with_confidence(cleaned)

        results: List[Dict[str, float | str]] = []
        for sentiment, confidence in predictions:
            results.append(
                {
                    "sentiment": sentiment,
                    "confidence": round(confidence, 3),
                }
            )
        return results

    def statistics(self, results: List[Dict[str, float | str]]) -> Dict[str, int]:
        sentiments = [r["sentiment"] for r in results]
        return dict(Counter(sentiments))
