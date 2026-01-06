[2026-01-06 06:36:24] Connected
[2026-01-06 06:36:24] main> SELECT t.*
                            FROM wallcons t
                            LIMIT 501
[2026-01-06 06:36:25] 9 rows retrieved starting from 1 in 394 ms (execution: 8 ms, fetching: 386 ms)
[2026-01-06 06:41:49] main> SELECT t.*
                            FROM wallcons t
                            LIMIT 501
[2026-01-06 06:41:49] 9 rows retrieved starting from 1 in 351 ms (execution: 6 ms, fetching: 345 ms)
[2026-01-06 06:45:39] main> DELETE FROM wallcons WHERE name = 'Ninguno'
[2026-01-06 06:45:39] 1 row affected in 9 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_StructuralFoundation' WHERE name = 'SOL CAM SANIT'
[2026-01-06 06:45:39] 1 row affected in 2 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_Walls' WHERE name = 'MURO EXTERIOR'
[2026-01-06 06:45:39] 1 row affected in 0 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_Floors' WHERE name = 'FOR INT AC-NH'
[2026-01-06 06:45:39] 1 row affected in 1 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_Walls' WHERE name = 'TAB INT'
[2026-01-06 06:45:39] 1 row affected in 1 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_Roofs' WHERE name = 'CUB IN TEJA'
[2026-01-06 06:45:39] 1 row affected in 0 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_Floors' WHERE name = 'FOR INT'
[2026-01-06 06:45:39] 1 row affected in 1 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_StructuralFoundation' WHERE name = 'FOR CAM SANIT'
[2026-01-06 06:45:39] 1 row affected in 2 ms
[2026-01-06 06:45:39] main> UPDATE wallcons SET revit_category = 'OST_Walls' WHERE name = 'MURO CAM SANIT'
[2026-01-06 06:45:39] 1 row affected in 1 ms
[2026-01-06 06:45:39] main> SELECT t.*
                            FROM wallcons t
                            LIMIT 501
[2026-01-06 06:45:39] 8 rows retrieved starting from 1 in 407 ms (execution: 13 ms, fetching: 394 ms)
