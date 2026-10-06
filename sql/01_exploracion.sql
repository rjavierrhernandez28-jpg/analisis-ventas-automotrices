-- 01. Exploración inicial
-- Ejecuta cada bloque por separado y escribe tus observaciones en el README.

-- ¿Cuántas ventas hay y en qué periodo?
SELECT
    COUNT(*) AS numero_ventas,
    MIN(fecha) AS primera_venta,
    MAX(fecha) AS ultima_venta
FROM ventas;

-- Revisa algunas filas y familiarízate con las columnas.
SELECT *
FROM ventas
ORDER BY fecha, id
LIMIT 10;

-- Comprueba que no existan valores faltantes en campos críticos.
SELECT
    SUM(CASE WHEN fecha IS NULL THEN 1 ELSE 0 END) AS fechas_faltantes,
    SUM(CASE WHEN precio_venta IS NULL THEN 1 ELSE 0 END) AS precios_faltantes,
    SUM(CASE WHEN costo_total IS NULL THEN 1 ELSE 0 END) AS costos_faltantes
FROM ventas;


