from src.model import SentimentModel

def test_model_prediction() -> None:
    model = SentimentModel()
    texts = ["good", "bad"]
    labels = ["positive", "negative"]
    model.train(texts, labels)

    prediction, confidence = model.predict_with_confidence(["good"])[0]
    assert prediction in {"positive", "negative"}
    assert 0.0 <= confidence <= 1.0
    