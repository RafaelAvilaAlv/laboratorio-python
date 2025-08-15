# Notas — Anotaciones de tipado (Parte C)

1) Las type hints documentan contratos (parámetros/retornos/variables) y mejoran autocompletado, refactors y detección temprana de errores.
2) No se validan en runtime por defecto: Python las ignora al ejecutar; la verificación la hacen herramientas como mypy/pyright.
3) En 3.12 los builtins son genéricos: list[int], dict[str, float], etc.
4) Union moderno: int | float (equivale a Union[int, float]); opcional: T | None (equivale a Optional[T]).
5) Ejemplos: variables tipadas, funciones (greet, average), Optional (parse_int), Union (safe_add) y colecciones opcionales (dedup_ids).
6) Beneficios reales: contratos claros, menos bugs en cambios grandes, documentación viva y mejores mensajes de IDE/CI.
7) Limitaciones: tipos no garantizan correctitud lógica ni validan datos externos sin checkers/validaciones.
8) Herramientas: mypy, pyright, pylance; integración frecuente en CI.
