SELECT
    sucursal,
    COUNT(*) AS unidades,
    ROUND(SUM(precio_venta), 2) AS ingresos,
    ROUND(SUM(utilidad), 2) AS utilidad,
    ROUND(100.0 * SUM(utilidad) / SUM(precio_venta), 2) AS margen_porcentaje
FROM ventas
WHERE modelo = 'Seal'
GROUP BY sucursal
ORDER BY utilidad DESC;