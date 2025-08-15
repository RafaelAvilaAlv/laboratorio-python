# ejercicio_a4.py
# Excepcion personalizada y validaciones de negocio para calcular_total

from __future__ import annotations


class CantidadInvalida(Exception):
    """Se lanza cuando la cantidad no es un entero > 0."""
    pass


def calcular_total(precio_unitario: float, cantidad: int) -> float:
    """
    Calcula el total = precio_unitario * cantidad validando entradas.

    Args:
        precio_unitario: Precio por unidad (debe ser >= 0).
        cantidad: Numero de unidades (debe ser entero > 0).

    Returns:
        Total como float.

    Raises:
        CantidadInvalida: si cantidad <= 0.
        ValueError: si precio_unitario < 0.
        TypeError: si tipos no son los esperados.
    """
    # Validaciones de tipo (explícitas para mensajes claros)
    if not isinstance(precio_unitario, (int, float)):
        raise TypeError("precio_unitario debe ser int o float")
    if not isinstance(cantidad, int):
        raise TypeError("cantidad debe ser int")

    # Reglas de negocio
    if cantidad <= 0:
        raise CantidadInvalida("cantidad debe ser > 0")
    if precio_unitario < 0:
        raise ValueError("precio_unitario no puede ser negativo")

    return float(precio_unitario) * cantidad


# --- Pruebas / demostracion ---
if __name__ == "__main__":
    # Caso OK
    print("Total (10 x 3) =", calcular_total(10, 3))  # 30.0

    # Manejo de errores con mensajes claros
    casos = [
        ("cantidad=0", (10, 0)),
        ("precio_unitario=-5", (-5, 2)),
        ("cantidad tipo incorrecto", (10, 2.5)),
        ("precio_unitario tipo incorrecto", ("10", 2)),
    ]

    for titulo, (p, c) in casos:
        try:
            print(f"\nCaso: {titulo}")
            print("Resultado:", calcular_total(p, c))
        except CantidadInvalida as e:
            print("Error de cantidad:", e)
        except ValueError as e:
            print("Error de valor:", e)
        except TypeError as e:
            print("Error de tipo:", e)

    # Aserciones minimas
    assert calcular_total(10, 3) == 30.0
    try:
        calcular_total(10, 0)
    except CantidadInvalida:
        pass
    else:
        raise AssertionError("Debio lanzar CantidadInvalida para cantidad=0")

    print("\n✔ Pruebas basicas OK")
