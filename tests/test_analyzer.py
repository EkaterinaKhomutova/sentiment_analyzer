from src.analyzer import SentimentAnalyzer

def test_statistics() -> None:
    analyzer = SentimentAnalyzer()
    results = [
        {"sentiment": "positive", "confidence": 0.9},
        {"sentiment": "negative", "confidence": 0.8},
        {"sentiment": "positive", "confidence": 0.7},
    ]
    stats = analyzer.statistics(results)
    assert stats["positive"] == 2
