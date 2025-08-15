# Notas — Paquetes (Parte B)

## Importaciones absolutas vs. relativas
- **Absolutas** (`import textkit.metrics`): se usan fuera del paquete o en el script principal; son claras y estables.
- **Relativas** (`from .clean import normalize`): se usan **dentro** del paquete para referenciar módulos hermanos sin acoplar al nombre externo del paquete.

## Qué expone `__init__.py` y por qué
- Reexporta funciones clave para una API pública simple:
  ```python
  from .clean import normalize, squeeze_spaces
  from .metrics import is_palindrome, token_count
  __all__ = ["normalize", "squeeze_spaces", "is_palindrome", "token_count"]
