from __future__ import annotations
import unicodedata

def normalize(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text debe ser str")
    s = text.strip().lower()
    s = ''.join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn")
    return s

def squeeze_spaces(text: str) -> str:
    return " ".join(text.split())
