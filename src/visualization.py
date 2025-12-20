from typing import Dict
import matplotlib.pyplot as plt

def plot_statistics(stats: Dict[str, int]) -> None:
    plt.bar(stats.keys(), stats.values())
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()
