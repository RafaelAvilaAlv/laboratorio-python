# === A.1 – Funciones como valores ===
# Usamos type hints para mayor claridad y PEP 8 para formato

from typing import Callable, Any


# 1. Definición de funciones simples
def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}"


def despedir(nombre: str) -> str:
    """Devuelve una despedida personalizada."""
    return f"Adiós, {nombre}"


def aplaudir(nombre: str) -> str:
    """Devuelve un mensaje de aplauso."""
    return f"👏👏 Bien hecho, {nombre}"


# 2. Diccionario que mapea nombres de acción a funciones
acciones: dict[str, Callable[..., Any]] = {
    "saludar": saludar,
    "despedir": despedir,
    "aplaudir": aplaudir
}


# 3. Función para ejecutar acciones
def ejecutar(accion: str, *args, **kwargs) -> Any:
    """
    Ejecuta la acción indicada, pasando argumentos variables.
    
    Args:
        accion: Nombre de la acción a ejecutar (clave del diccionario acciones).
        *args: Argumentos posicionales para la función.
        **kwargs: Argumentos con nombre para la función.
    
    Returns:
        El resultado de la función llamada.
    
    Raises:
        KeyError: Si la acción no existe en el diccionario.
    """
    if accion not in acciones:
        raise KeyError(f"Acción '{accion}' no encontrada. Opciones válidas: {list(acciones.keys())}")
    funcion = acciones[accion]
    return funcion(*args, **kwargs)


# 4. Ejemplos de uso
if __name__ == "__main__":
    print(ejecutar("saludar", "Ana"))      # Hola, Ana
    print(ejecutar("despedir", "Luis"))    # Adiós, Luis
    print(ejecutar("aplaudir", "Marta"))   # 👏👏 Bien hecho, Marta

    # Ejemplo de acción inexistente
    try:
        ejecutar("bailar", "Pedro")
    except KeyError as e:
        print(f"Error: {e}")
