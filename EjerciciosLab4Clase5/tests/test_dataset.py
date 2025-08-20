import csv
from pathlib import Path

DATA = Path("data/dataset.csv")

def test_csv_tiene_columnas_obligatorias():
    with DATA.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = set(reader.fieldnames or [])
        assert {"id", "nombre", "valor"}.issubset(cols)

def test_csv_reglas_basicas():
    ids = set()
    n_rows = 0
    with DATA.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            n_rows += 1
            # id: no vacío y único
            assert row["id"]
            assert row["id"] not in ids
            ids.add(row["id"])
            # nombre: no vacío (sin solo espacios)
            assert row["nombre"].strip() != ""
            # valor: convertible a número y no negativo
            valor = float(row["valor"])
            assert valor >= 0
    assert n_rows > 0
