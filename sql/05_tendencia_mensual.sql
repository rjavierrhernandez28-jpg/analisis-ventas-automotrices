SELECT
    strftime('%Y-%m', fecha) AS mes,
    COUNT(*) AS unidades,
    ROUND(SUM(precio_venta), 2) AS ingresos,
    ROUND(SUM(utilidad), 2) AS utilidad,
    ROUND(100.0 * SUM(utilidad) / SUM(precio_venta), 2) AS margen_porcentaje
FROM ventas
GROUP BY strftime('%Y-%m', fecha)
ORDER BY mes;