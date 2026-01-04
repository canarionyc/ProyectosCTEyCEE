CREATE OR REPLACE FUNCTION numpy_matrix_mult(mat_a float[][], mat_b float[][])
RETURNS float[][]
AS $$
    import numpy as np

    # 1. Convert PostgreSQL arrays (lists of lists) to Numpy Arrays
    #    Postgres passes multidimensional arrays as nested lists
    a = np.array(mat_a)
    b = np.array(mat_b)

    # 2. Perform Matrix Multiplication (Dot Product)
    try:
        result = np.dot(a, b)
    except ValueError as e:
        plpy.error(f"Matrix dimension mismatch: {e}")

    # 3. Convert back to Python List so Postgres can read it
    return result.tolist()
$$ LANGUAGE plpython3u;

SELECT numpy_matrix_mult(
    ARRAY[[1, 2], [3, 4]],
    ARRAY[[2, 0], [1, 2]]
) AS stress_transformation;