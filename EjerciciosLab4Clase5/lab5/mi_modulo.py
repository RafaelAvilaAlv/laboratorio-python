from __future__ import annotations
from datetime import date
from typing import Union

Number = Union[int, float]

def normalizar_texto(s: str) -> str:
    """Quita espacios duplicados y baja a minúsculas."""
    if not isinstance(s, str):
        raise TypeError("s debe ser str")
    return " ".join(s.strip().split()).lower()

def porcentaje_cambio(actual: Number, base: Number) -> float:
    """(actual - base) / base. ZeroDivisionError si base == 0."""
    if float(base) == 0.0:
        raise ZeroDivisionError("base no puede ser 0")
    return (float(actual) - float(base)) / float(base)

def parse_fecha_iso(s: str) -> date:
    """Parsea 'YYYY-MM-DD' o levanta ValueError. TypeError si no es str."""
    if not isinstance(s, str):
        raise TypeError("s debe ser str")
    return date.fromisoformat(s)
