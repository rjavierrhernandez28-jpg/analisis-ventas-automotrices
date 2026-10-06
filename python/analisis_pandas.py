from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
RUTA_DATOS = RAIZ / "data" / "raw" / "ventas_automotrices.csv"

ventas = pd.read_csv(RUTA_DATOS)
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

print("Primeras cinco ventas:")
print(ventas.head())

print(f"\nFilas: {ventas.shape[0]} | Columnas: {ventas.shape[1]}")

print("\nTipos de datos:")
print(ventas.dtypes)