import pandas as pd

# Lee CSV (utf-8-sig por si trae BOM) y parsea fechas
df = pd.read_csv("data/ventas.csv", encoding="utf-8-sig", parse_dates=["fecha"])

print("HEAD:\n", df.head(), "\n")
print(df.info(), "\n")
print("NULOS:\n", df.isna().sum(), "\n")

# Derivadas + agregación
out = (
    df.assign(
        precio_con_iva=lambda d: d["precio"] * 1.12,
        mes=lambda d: d["fecha"].dt.to_period("M").astype(str),
    )
    .query("categoria == \"A\"")
    .groupby("cliente", as_index=False)
    .agg(total=("monto","sum"), n=("monto","size"), promedio=("monto","mean"))
    .sort_values("total", ascending=False)
)

out.to_parquet("outputs/resumen_pandas.parquet", index=False)
print("RESUMEN PANDAS:\n", out.head())
