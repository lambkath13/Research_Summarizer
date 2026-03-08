import re


def clean_text(text):

    text = re.sub(r'\[[0-9]+\]', '', text)

    text = re.sub(r'Fig\.\s*\d+.*?', '', text)

    text = re.sub(r'Table\s*\d+.*?', '', text)

    text = re.sub(r'References.*', '', text, flags=re.IGNORECASE)

    text = re.sub(r'\s+', ' ', text)

    return text