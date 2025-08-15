# Módulo: string_utils (Utilidades de cadenas)

## API pública
- `normalize(text, *, to_lower=True, strip=True, remove_accents=True) -> str`  
  Normaliza cadenas (espacios, minúsculas, acentos).
- `is_palindrome(text, *, ignore_case=True, ignore_spaces=True) -> bool`  
  Verifica palíndromos con opciones de normalización.
- `title_case(name) -> str`  
  Convierte nombres a Título, respetando conectores comunes (de, del, la, etc.).
- `safe_truncate(text, max_len, *, ellipsis="…") -> str`  
  Trunca texto de forma segura y valida parámetros (lanza `ValueError` en casos límite).

## ¿Por qué separarlo como módulo independiente?
- Reúne **funciones coherentes de cadenas** que pueden reutilizarse en distintos scripts.
- Facilita **mantenimiento y pruebas** (cada función tiene responsabilidad clara).
- Permite **importar solo lo necesario** desde otros puntos de entrada.

## Caso límite probado y documentado
- `safe_truncate("Hola", 1, ellipsis="…")` → lanza `ValueError` (el largo del ellipsis ≥ max_len).

## Referencia oficial
- **Modules — Python 3.12 Docs**: https://docs.python.org/3.12/tutorial/modules.html
