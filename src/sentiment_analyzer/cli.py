# Должен быть в корне src - см. пример в проекте, который мы писали на паре "под ключ"


import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sentiment Analyzer")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to CSV file with texts",
    )
    return parser.parse_args()
