-- 1. Enable the Python Language extension
-- (If this fails, your Python path/DLL setup from the previous step needs checking)
CREATE EXTENSION IF NOT EXISTS plpython3u;

-- 2. Define the Dot Product function using Python
CREATE OR REPLACE FUNCTION py_dot_product(vec_a float[], vec_b float[])
RETURNS float
AS $$
    # Check if vectors are same length
    if len(vec_a) != len(vec_b):
        plpy.error("Vectors must be the same length")

    # Calculate Dot Product using pure Python
    # (We use zip() to pair the elements and sum() to add the products)
    result = sum(a * b for a, b in zip(vec_a, vec_b))

    return result
$$ LANGUAGE plpython3u;

SELECT py_dot_product(ARRAY[10, 20, 5], ARRAY[2, 0, 4]) AS work_done;