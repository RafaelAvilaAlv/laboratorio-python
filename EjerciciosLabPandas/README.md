# EjerciciosLabPandas

Análisis de un CSV de ventas usando **Pandas** y **DuckDB**.  
Se generan resúmenes por cliente y se guarda el resultado en `outputs/`.

## Requisitos
- Python 3.12+
- (Opcional) Git para versionar

## Instalación

> Recomendado: usar un entorno virtual


### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install -r requirements.txt




Estructura del proyecto
EjerciciosLabPandas/
├─ data/
│  ├─ ventas.csv
│  └─ ventas_clean.csv          # CSV limpio usado por los scripts
├─ outputs/
│  └─ resumen_duckdb.csv        # (se genera al correr duckdb_run.py)
├─ duckdb_run.py
├─ pandas_run.py
├─ requirements.txt
└─ README.md



Ejecución
A) Pandas

Lee el CSV, muestra un resumen (head, info, nulos) y calcula agregados por cliente.

python pandas_run.py


Salida esperada: imprime por consola y (si el script lo hace) guarda un Parquet/CSV en outputs/.

B) DuckDB

Lee el CSV con esquema explícito (sin auto-detección), filtra categoria='A', agrega por cliente y ordena.

python duckdb_run.py


Salida: outputs/resumen_duckdb.csv

Notas técnicas

El CSV puede incluir BOM; Pandas usa encoding='utf-8-sig'.

En DuckDB se usa read_csv con:

header=true, delim=',', quote='', escape=''

dateformat='%Y-%m-%d'

auto_detect=false (no “olfatea” el esquema)

ignore_errors=true (si alguna fila está mal formateada, se omite)

Tipos de columna forzados: cliente (VARCHAR), categoria (VARCHAR), monto (DOUBLE), precio (DOUBLE), fecha (DATE).

Comandos útiles

Ver primeras líneas del CSV de salida:

Get-Content outputs\resumen_duckdb.csv -TotalCount 10


Listar paquetes instalados:

pip list


Actualizar dependencias (si fuera necesario):

pip install -r requirements.txt --upgrade

Troubleshooting

Si DuckDB muestra error de “sniffing” o separador incorrecto, confirma que el CSV limpio tenga coma , como delimitador y fecha YYYY-MM-DD.

Si aparece BOM, vuelve a grabar el CSV como UTF-8 sin BOM:

(Get-Content data\ventas_clean.csv -Raw) | Set-Content -Encoding utf8 data\ventas_clean.csv


"@ | Set-Content -Encoding utf8 README.md

Verifica

Get-Content README.md -TotalCount 20


Es un mini-ejercicio de análisis de ventas a partir de un CSV con columnas cliente, categoria, monto,
precio y fecha. Se leen y validan los datos (head, info y nulos), y se calcula un resumen por cliente con el total vendido,
el número de compras y el promedio del monto, primero con Pandas y luego con DuckDB/SQL para comparar enfoques;
los resultados se exportan a outputs/ (CSV/Parquet). El dataset tiene 10 registros de las categorías A y B en mayo, con clientes como C001–C006.
