# Análisis de ventas automotrices

Proyecto de portafolio para demostrar un flujo de trabajo de analista de datos:

1. generar datos de ventas reproducibles;
2. almacenarlos y consultarlos con SQLite/SQL;
3. analizar hallazgos con Python/Pandas;
4. crear un dashboard en Power BI.

> Los datos son sintéticos. Fueron creados para fines de aprendizaje y portafolio; no representan ventas reales.

## Preguntas de negocio

- ¿Cómo evolucionan ingresos, unidades y utilidad por mes?
- ¿Qué sucursales, vendedores y modelos generan mayor utilidad?
- ¿Qué productos tienen mejor margen y cuáles requieren atención?
- ¿Hay patrones estacionales o diferencias entre regiones?

## Estructura

```text
data/raw/          # fuente generada; no se modifica manualmente
data/processed/    # exportaciones listas para análisis o Power BI
sql/               # consultas SQL numeradas y explicadas
python/            # generación y análisis con Python
dashboard/         # archivo .pbix y capturas del dashboard
```

## Primer paso

Ejecuta desde la raíz del proyecto:

```powershell
py python/generar_datos.py
```

Esto creará `data/raw/ventas_automotrices.csv` y `data/ventas_automotrices.db`.

Después abre la base con una extensión de SQLite en VS Code o DB Browser for SQLite y ejecuta las consultas de `sql/` una por una.

## Hallazgos iniciales

A primera vista se puede apreciar que del 2024 al 2025 las ventas en general bajaron, puesto que se vendieron menos unidades. Sin embargo, las unidades que se vendieron lograron amortiguar un poco la situación, ya que los ingresos son cercanos, aunque  aún así la diferencia en utilidad entre ambos años fué de aproximadamente 4 millones. 

Las sucursales que más destacaron fueron Coatzacoalcos y minatitlán liderando las ventas de unidades, así como la utilidad y los ingresos, durante los dos años.

El modelo estrella de estos años fué el BYD Seal, que tuvo sus mayores ventas entre Coatzacoalcos, Acayucan y Minatitlan, dejando muy buena utilidad entre ellos. 

El detalle central está en la baja de las ventas entre 2024 y 2025 que comienza justo en los últimos meses del 2024. 

Mi propuesta sería indagar más a contra año a cada sucursal, marca y vendedor para poder descubrir el area de oportunidad que tenemos que mejorar.
