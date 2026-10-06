"""Genera un dataset sintético, reproducible y apto para practicar análisis."""

from __future__ import annotations

import csv
import random
import sqlite3
from datetime import date, timedelta
from pathlib import Path


# Usar una semilla fija significa que cualquier persona puede recrear los mismos datos.
RANDOM_SEED = 20260831
NUMERO_VENTAS = 1500
RAIZ = Path(__file__).resolve().parents[1]
RUTA_CSV = RAIZ / "data" / "raw" / "ventas_automotrices.csv"
RUTA_BD = RAIZ / "data" / "ventas_automotrices.db"

SUCURSALES = {
    "Acayucan": "Sur",
    "Coatzacoalcos": "Sur",
    "Minatitlán": "Sur",
    "Veracruz": "Centro",
    "Xalapa": "Centro",
}
VENDEDORES = {
    "Acayucan": ["Carlos Hernández", "Sofía Martínez"],
    "Coatzacoalcos": ["Ana López", "Jorge Ramírez"],
    "Minatitlán": ["Pedro García", "Valeria Cruz"],
    "Veracruz": ["Diego Torres", "Mariana Flores"],
    "Xalapa": ["Luis Mendoza", "Camila Reyes"],
}
MODELOS = [
    ("Toyota", "Avanza", "SUV", 378_000, 0.13),
    ("Toyota", "Hilux", "Pickup", 590_000, 0.15),
    ("Toyota", "Corolla", "Sedán", 455_000, 0.12),
    ("BYD", "Dolphin", "Eléctrico", 535_000, 0.16),
    ("BYD", "Seal", "Eléctrico", 780_000, 0.17),
    ("Suzuki", "Swift", "Hatchback", 340_000, 0.11),
    ("Mazda", "CX-5", "SUV", 610_000, 0.14),
    ("Nissan", "Versa", "Sedán", 390_000, 0.10),
]
CANALES = ["Piso de venta", "Digital", "Referido", "Flotilla"]


def generar_ventas() -> list[dict[str, object]]:
    random.seed(RANDOM_SEED)
    inicio = date(2024, 1, 1)
    dias = (date(2025, 12, 31) - inicio).days
    ventas = []

    for identificador in range(1, NUMERO_VENTAS + 1):
        marca, modelo, segmento, precio_lista, margen_base = random.choice(MODELOS)
        fecha = inicio + timedelta(days=random.randint(0, dias))
        sucursal = random.choice(list(SUCURSALES))
        descuento = round(precio_lista * random.uniform(0, 0.07), 2)
        precio_venta = round(precio_lista - descuento, 2)
        costo_total = round(precio_venta * (1 - margen_base + random.uniform(-0.025, 0.025)), 2)
        utilidad = round(precio_venta - costo_total, 2)

        ventas.append(
            {
                "id": identificador,
                "fecha": fecha.isoformat(),
                "sucursal": sucursal,
                "region": SUCURSALES[sucursal],
                "vendedor": random.choice(VENDEDORES[sucursal]),
                "canal": random.choice(CANALES),
                "marca": marca,
                "modelo": modelo,
                "segmento": segmento,
                "precio_lista": precio_lista,
                "descuento": descuento,
                "precio_venta": precio_venta,
                "costo_total": costo_total,
                "utilidad": utilidad,
            }
        )
    return ventas


def guardar(ventas: list[dict[str, object]]) -> None:
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=ventas[0].keys())
        escritor.writeheader()
        escritor.writerows(ventas)

    with sqlite3.connect(RUTA_BD) as conexion:
        conexion.execute("DROP TABLE IF EXISTS ventas")
        # Tipos explícitos: fechas y categorías son texto; importes, números.
        conexion.execute(
            """CREATE TABLE ventas (
                id INTEGER PRIMARY KEY,
                fecha TEXT NOT NULL,
                sucursal TEXT NOT NULL,
                region TEXT NOT NULL,
                vendedor TEXT NOT NULL,
                canal TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                segmento TEXT NOT NULL,
                precio_lista REAL NOT NULL,
                descuento REAL NOT NULL,
                precio_venta REAL NOT NULL,
                costo_total REAL NOT NULL,
                utilidad REAL NOT NULL
            )"""
        )
        conexion.executemany(
            """INSERT INTO ventas VALUES
            (:id, :fecha, :sucursal, :region, :vendedor, :canal, :marca, :modelo,
             :segmento, :precio_lista, :descuento, :precio_venta, :costo_total, :utilidad)""",
            ventas,
        )
        conexion.execute("CREATE INDEX idx_ventas_fecha ON ventas(fecha)")
        conexion.execute("CREATE INDEX idx_ventas_sucursal ON ventas(sucursal)")


if __name__ == "__main__":
    ventas_generadas = generar_ventas()
    guardar(ventas_generadas)
    print(f"Listo: {len(ventas_generadas)} ventas en {RUTA_CSV.name} y {RUTA_BD.name}.")
