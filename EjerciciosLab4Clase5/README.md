# Lab Clase 5 — Pytest + CSV (Python 3.12)

Práctica en dos partes:
- **Parte A:** módulo sencillo con funciones y **tests** con `pytest`.
- **Parte B:** validación de un **CSV** usando la **librería estándar** `csv` (sin pandas) y `pytest`.

---

## Requisitos
- Python **3.12** (recomendado)
- `pip`

---

## Instalación (Windows / PowerShell)
```ps1
# 1) Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate

# 2) Instalar dependencias
python -m pip install -U pip
python -m pip install -r requirements.txt


Ejecutar las pruebas

Todas las pruebas

pytest -q


Solo Parte A (módulo)

pytest -q -k mi_modulo


Solo Parte B (CSV)

pytest -q -k dataset



Estructura del proyecto

Si usaste src/ en lugar de lab5/, cambia el nombre en esta sección y en los imports de los tests.

.
├─ lab5/
│  └─ mi_modulo.py
├─ data/
│  └─ dataset.csv
├─ tests/
│  ├─ test_mi_modulo.py
│  └─ test_dataset.py
├─ requirements.txt
└─ README.md



Parte A — Módulo probado con pytest

Archivo: lab5/mi_modulo.py
Funciones implementadas:

normalizar_texto(s: str) -> str
Limpia espacios duplicados y pasa a minúsculas.

Errores: TypeError si s no es str.

porcentaje_cambio(actual, base) -> float
Calcula (actual - base) / base.

Errores: ZeroDivisionError si base == 0.

parse_fecha_iso(s: str) -> datetime.date
Parsea fechas en formato YYYY-MM-DD.

Errores: TypeError si s no es str y ValueError si el formato es inválido.

Pruebas: tests/test_mi_modulo.py
Cubre:

Casos válidos (incluye fecha bisiesta).

Casos límite (cadenas vacías, espacios).

Errores esperados (TypeError, ValueError, ZeroDivisionError).



Parte B — Validación de CSV con csv (stdlib)

Dataset: data/dataset.csv
Pruebas: tests/test_dataset.py
Reglas validadas:

Columnas obligatorias: id, nombre, valor.

id: no vacío y único.

nombre: no vacío (sin solo espacios).

valor: convertible a float y no negativo.

Nota: los tests abren el archivo con encoding="utf-8-sig" para tolerar CSVs con BOM (común en Windows/Excel).

Personalización

Puedes reemplazar data/dataset.csv por tu propio archivo.

Si cambian las columnas o las reglas, edita tests/test_dataset.py.

Ideas de reglas extra:

id numérico y consecutivo.

valor dentro de un rango (p. ej. 0 <= valor <= 100).

Columna fecha válida:

from datetime import date
date.fromisoformat(row["fecha"])  # ValueError si no es YYYY-MM-DD


Problemas comunes
1) KeyError: 'id' o aparece '\ufeffid'

Tu CSV tiene BOM. Soluciones:

Mantener los tests con encoding="utf-8-sig" (ya está así), o

Regrabar el CSV sin BOM.

2) ModuleNotFoundError al importar lab5/src

Asegúrate de:

Ejecutar pytest desde la raíz del proyecto (donde están lab5/, tests/, data/).

Tener un __init__.py dentro de lab5/ o src/ si usas imports de paquete.

Cómo fue probado

Entorno virtual con Python 3.12.

pytest ejecutado con:

pytest -q


Resultado esperado: todos los tests en verde.



práctica en Python dividida en dos partes:
(A) crear un módulo simple y cubrirlo con tests de pytest (incluye funciones para normalizar texto,
calcular porcentaje de cambio y parsear fechas, con casos válidos, límites y errores esperados); y
(B) validar un CSV con la librería estándar csv (sin pandas), comprobando columnas obligatorias y
reglas como id único/no vacío y valor numérico no negativo. Se ejecuta en un venv, instala dependencias con requirements.txt,
corre tests con pytest -q, y está organizada en lab5/, data/ y tests/, con manejo de UTF-8-SIG para CSVs con BOM. 
