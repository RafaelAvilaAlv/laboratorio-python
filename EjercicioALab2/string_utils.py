# string_utils.py
# Módulo: utilidades de cadenas (normalizar, validar, formatear, truncar)
from __future__ import annotations
import unicodedata

def normalize(text: str, *, to_lower: bool = True, strip: bool = True, remove_accents: bool = True) -> str:
    """
    Normaliza una cadena:
      - strip: recorta espacios al inicio/fin.
      - to_lower: pasa a minúsculas.
      - remove_accents: elimina tildes/acentos (NFD → ASCII).
    """
    if not isinstance(text, str):
        raise TypeError("text debe ser str")

    out = text
    if strip:
        out = out.strip()
    if to_lower:
        out = out.lower()
    if remove_accents:
        # normaliza en NFD y elimina marcas diacríticas
        out = ''.join(c for c in unicodedata.normalize("NFD", out) if unicodedata.category(c) != "Mn")
    return out

def is_palindrome(text: str, *, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Devuelve True si 'text' es palíndromo, con opciones para ignorar mayúsculas/espacios.
    """
    if not isinstance(text, str):
        raise TypeError("text debe ser str")

    s = text
    if ignore_case:
        s = s.casefold()
    if ignore_spaces:
        s = ''.join(ch for ch in s if not ch.isspace())
    return s == s[::-1]

def title_case(name: str) -> str:
    """
    Convierte un nombre en 'Title Case' de forma simple, respetando conectores comunes.
    """
    if not isinstance(name, str):
        raise TypeError("name debe ser str")

    small_words = {"de", "del", "la", "los", "las", "y", "o", "u"}
    parts = normalize(name, to_lower=True, strip=True, remove_accents=False).split()
    if not parts:
        return ""

    titled: list[str] = []
    for i, w in enumerate(parts):
        if i != 0 and w in small_words:
            titled.append(w)  # minúscula intermedia
        else:
            titled.append(w[:1].upper() + w[1:])
    return " ".join(titled)

def safe_truncate(text: str, max_len: int, *, ellipsis: str = "…") -> str:
    """
    Trunca 'text' a como máximo 'max_len' caracteres.
    - Si 'text' cabe, se devuelve igual.
    - Si no cabe, se devuelve el recorte con un 'ellipsis' al final.
    Reglas/validación:
      - max_len debe ser >= 1.
      - Si max_len <= len(ellipsis), se lanza ValueError (no tendría sentido).
    """
    if not isinstance(text, str):
        raise TypeError("text debe ser str")
    if not isinstance(max_len, int):
        raise TypeError("max_len debe ser int")
    if max_len < 1:
        raise ValueError("max_len debe ser >= 1")
    if max_len <= len(ellipsis):
        raise ValueError("max_len debe ser mayor que la longitud del ellipsis")

    if len(text) <= max_len:
        return text
    return text[: max_len - len(ellipsis)] + ellipsis
