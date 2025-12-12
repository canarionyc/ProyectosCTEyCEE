SELECT t.*
FROM main.consolidated_consumption t
WHERE servicio = 'CAL'
ORDER BY proyecto;