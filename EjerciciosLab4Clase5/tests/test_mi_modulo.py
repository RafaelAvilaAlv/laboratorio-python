# mypy: ignore-errors
import pytest
from datetime import date
from lab5.mi_modulo import normalizar_texto, porcentaje_cambio, parse_fecha_iso

# --- normalizar_texto ---
@pytest.mark.parametrize(
    "entrada,esperado",
    [("  Hola   MUndo ", "hola mundo"), ("", ""), ("   ", "")],
)
def test_normalizar_texto_ok(entrada, esperado):
    assert normalizar_texto(entrada) == esperado

@pytest.mark.parametrize("entrada", [None, 123, 1.2])
def test_normalizar_texto_tipo_invalido(entrada):
    with pytest.raises(TypeError):
        normalizar_texto(entrada)  # type: ignore[arg-type]

# --- porcentaje_cambio ---
def test_porcentaje_cambio_ok():
    assert porcentaje_cambio(120, 100) == 0.2

def test_porcentaje_cambio_base_cero():
    with pytest.raises(ZeroDivisionError):
        porcentaje_cambio(10, 0)

# --- parse_fecha_iso ---
def test_parse_fecha_iso_ok():
    assert parse_fecha_iso("2024-02-29") == date(2024, 2, 29)

@pytest.mark.parametrize("mala", ["2023-02-29", "2024/01/01", ""])
def test_parse_fecha_iso_invalida(mala):
    with pytest.raises(ValueError):
        parse_fecha_iso(mala)

def test_parse_fecha_iso_tipo_invalido():
    with pytest.raises(TypeError):
        parse_fecha_iso(None)  # type: ignore[arg-type]
