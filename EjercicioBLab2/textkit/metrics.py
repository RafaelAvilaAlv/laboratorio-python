from __future__ import annotations
from .clean import normalize  # ← importación relativa

def is_palindrome(text: str) -> bool:
    s = normalize(text).replace(" ", "")
    return s == s[::-1]

def token_count(text: str) -> int:
    return len(normalize(text).split())
