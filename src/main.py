import logging
import pandas as pd  # pandas нет в зависимостях

from cli import parse_args
from analyzer import SentimentAnalyzer
from visualization import plot_statistics

logging.basicConfig(level=logging.INFO)

def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)

    texts = df["text"].tolist()

    analyzer = SentimentAnalyzer()
    results = analyzer.analyze(texts)
    stats = analyzer.statistics(results)

    print("Sentiment statistics:")
    for k, v in stats.items():
        print(f"{k}: {v}")

    plot_statistics(stats)

if __name__ == "__main__":
    main()
