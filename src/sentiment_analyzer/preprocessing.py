"""
Text preprocessing utilities.
"""

import re


def clean_text(text: str) -> str:
    """
    Normalize input text.

    Converts text to lowercase and removes punctuation.

    :param text: Raw input text
    :return: Cleaned text
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text
