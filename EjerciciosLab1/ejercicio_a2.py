from typing import Callable

def crear_descuento(porcentaje: float) -> Callable[[float], float]:
    if not isinstance(porcentaje, (int, float)):
        raise TypeError("porcentaje debe ser numérico")
    if not (0 <= porcentaje <= 1):
        raise ValueError("porcentaje debe estar entre 0 y 1")

    def aplicar(precio: float) -> float:
        if not isinstance(precio, (int, float)):
            raise TypeError("precio debe ser numérico")
        return float(precio) * (1 - float(porcentaje))
    return aplicar

if __name__ == "__main__":
    descuento10 = crear_descuento(0.10)
    descuento25 = crear_descuento(0.25)
    print(descuento10(100))  # 90.0
    print(descuento25(80))   # 60.0
