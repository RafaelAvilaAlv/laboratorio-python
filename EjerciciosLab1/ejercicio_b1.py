# ejercicio_a3.py
# Parseo robusto de enteros: continúa aunque existan errores.
# Devuelve (valores_convertidos, errores_encontrados)

from typing import List, Tuple


def parsear_enteros(entradas: List[str]) -> Tuple[List[int], List[str]]:
    """
    Convierte cada string de 'entradas' a int.
    Si algún elemento no es convertible, registra un mensaje de error,
    pero continúa con el resto.

    Returns:
        (valores, errores)
        - valores: lista de ints convertidos exitosamente.
        - errores: lista de mensajes de error con índice y valor problemático.
    """
    valores: List[int] = []
    errores: List[str] = []

    for i, s in enumerate(entradas):
        try:
            valores.append(int(s))
        except ValueError:
            errores.append(f"Ítem {i} = {s!r}: no es un entero válido")

    return valores, errores


# --- Pruebas rápidas / demostración ---
if __name__ == "__main__":
    datos = ["10", "x", "3", "  20", "7.5", "-8", "once"]
    valores, errores = parsear_enteros(datos)

    print("Entrada: ", datos)
    print("Valores:", valores)     # esperado: [10, 3, 20, -8]
    print("Errores:")
    for e in errores:
        print(" -", e)

    # Aserciones mínimas (fallan si el comportamiento no es el esperado)
    assert valores == [10, 3, 20, -8]
    assert any("x" in e for e in errores)
    assert any("7.5" in e for e in errores)
    assert any("once" in e for e in errores)
    print("\n✔ Pruebas básicas OK")
