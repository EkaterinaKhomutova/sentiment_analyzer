"""
Machine learning model for sentiment analysis.
"""

from typing import List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer  # sklearn нет в зависимостях
from sklearn.linear_model import LogisticRegression


class SentimentModel:
    """
    TF-IDF + Logistic Regression sentiment classifier.
    """

    def __init__(self) -> None:
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression(max_iter=200)

    def train(self, texts: List[str], labels: List[str]) -> None:
        """
        Train the sentiment model.

        :param texts: Training texts
        :param labels: Corresponding sentiment labels
        """
        features = self.vectorizer.fit_transform(texts)
        self.model.fit(features, labels)

    def predict_with_confidence(
        self, texts: List[str]
    ) -> List[Tuple[str, float]]:
        """
        Predict sentiment with confidence score.

        :param texts: Input texts
        :return: List of (sentiment, confidence)
        """
        features = self.vectorizer.transform(texts)
        probabilities = self.model.predict_proba(features)

        predictions = self.model.classes_[probabilities.argmax(axis=1)]
        confidences = probabilities.max(axis=1)

        return list(zip(predictions.tolist(), confidences.tolist()))
