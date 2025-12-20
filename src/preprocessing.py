import re

def clean_text(text: str) -> str:
    """
    Remove punctuation and convert text to lowercase.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text
