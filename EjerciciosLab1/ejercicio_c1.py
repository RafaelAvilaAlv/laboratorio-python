# ejercicio_c1.py
# Decorador requiere_positivos: asegura que todos los args sean positivos

from functools import wraps

def requiere_positivos(func):
    """
    Decorador que verifica que todos los argumentos numéricos sean > 0.
    Si no lo son, lanza ValueError.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Comprobamos todos los argumentos
        for i, arg in enumerate(list(args) + list(kwargs.values()), start=1):
            if isinstance(arg, (int, float)):
                if arg <= 0:
                    raise ValueError(f"Argumento #{i} debe ser positivo: {arg}")
        return func(*args, **kwargs)
    return wrapper

# --- Ejemplos de uso ---
@requiere_positivos
def calcular_area_rectangulo(base, altura):
    return base * altura

@requiere_positivos
def sumar(a, b):
    return a + b


if __name__ == "__main__":
    # Casos válidos
    print("Área 5x3 =", calcular_area_rectangulo(5, 3))
    print("Suma 10 + 20 =", sumar(10, 20))

    # Casos inválidos
    pruebas = [
        ("Base negativa", calcular_area_rectangulo, (-5, 3)),
        ("Altura cero", calcular_area_rectangulo, (5, 0)),
        ("Suma con negativo", sumar, (10, -4)),
    ]

    for titulo, func, params in pruebas:
        try:
            print(f"\nCaso: {titulo}")
            print("Resultado:", func(*params))
        except ValueError as e:
            print("Error:", e)

    print("\n✔ Pruebas basicas OK")
