-- 02. KPIs principales
-- Cada fila representa la venta de un vehículo.

SELECT
    COUNT(*) AS unidades_vendidas,
    ROUND(SUM(precio_venta), 2) AS ingresos,
    ROUND(SUM(utilidad), 2) AS utilidad,
    ROUND(100.0 * SUM(utilidad) / SUM(precio_venta), 2) AS margen_porcentaje,
    ROUND(AVG(precio_venta), 2) AS ticket_promedio
FROM ventas;

-- Comparación de desempeño entre sucursales.
SELECT
    sucursal,
    COUNT(*) AS unidades,
    ROUND(SUM(precio_venta), 2) AS ingresos,
    ROUND(SUM(utilidad), 2) AS utilidad,
    ROUND(100.0 * SUM(utilidad) / SUM(precio_venta), 2) AS margen_porcentaje
FROM ventas
GROUP BY sucursal
ORDER BY utilidad DESC;
