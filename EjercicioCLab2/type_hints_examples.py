# type_hints_examples.py
from __future__ import annotations
from typing import Optional  # En 3.12 también puedes usar | None (PEP 604)

# Variables tipadas
user: str = "Ana"
scores: list[int] = [10, 9, 8]

# Funciones con tipos básicos
def greet(name: str) -> str:
    return f"Hola, {name}"

def average(values: list[float]) -> float:
    if not values:
        raise ValueError("values no puede estar vacío")
    return sum(values) / len(values)

# Optional / Union (PEP 604: int | float, y Optional[T] == T | None)
def parse_int(text: str) -> Optional[int]:
    try:
        return int(text)
    except ValueError:
        return None  # None indica que no se pudo convertir

def safe_add(a: int | float, b: int | float) -> float:
    return float(a) + float(b)

# Combinar Optional con colecciones
def dedup_ids(ids: list[int] | None) -> list[int]:
    if ids is None:
        return []
    return list(dict.fromkeys(ids))  # elimina duplicados preservando orden

if __name__ == "__main__":
    print(greet(user))                       # Hola, Ana
    print(average([1.0, 2.0, 3.0]))          # 2.0
    print(parse_int("123"), parse_int("x"))  # 123 None
    print(safe_add(3, 4.5))                  # 7.5
    print(dedup_ids([1, 2, 2, 3]))           # [1, 2, 3]
