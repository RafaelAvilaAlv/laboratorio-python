import duckdb
from pathlib import Path

# Ruta absoluta en formato POSIX (evita problemas de backslashes)
csv_path = (Path(__file__).parent / "data" / "ventas_clean.csv").resolve().as_posix()
csv_path_sql = csv_path.replace("'", "''")  # por si hubiese comillas simples

sql = f"""
CREATE OR REPLACE TABLE resumen AS
SELECT
  cliente,
  SUM(monto)   AS total,
  COUNT(*)     AS n,
  AVG(monto)   AS promedio
FROM read_csv(
  '{csv_path_sql}',
  columns={{
    'cliente'  : 'VARCHAR',
    'categoria': 'VARCHAR',
    'monto'    : 'DOUBLE',
    'precio'   : 'DOUBLE',
    'fecha'    : 'DATE'
  }},
  header       = true,
  delim        = ',',
  dateformat   = '%Y-%m-%d',
  auto_detect  = false,     -- no olfatees nada
  strict_mode  = false,     -- tolera CSV no-perfecto
  ignore_errors= true       -- si algo raro aparece en alguna fila, sáltala
)
WHERE categoria = 'A'
GROUP BY cliente
ORDER BY total DESC;
"""

duckdb.sql(sql)
duckdb.sql("COPY resumen TO 'outputs/resumen_duckdb.csv' (HEADER, DELIMITER ',');")
print("DuckDB TOP 5:")
duckdb.sql("SELECT * FROM resumen LIMIT 5;").show()
