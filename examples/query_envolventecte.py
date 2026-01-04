import duckdb

# The path to your JSON file
json_file_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/envolventecte-6716947208413769375.json'

# Connect to an in-memory DuckDB database
con = duckdb.connect()

# Query the 'walls' array directly from the JSON file
# The table name is the file path, and you can use dot notation to access nested arrays.
query = f"""
SELECT 
    name, 
    bounds,
    geometry.tilt,
    geometry.azimuth
FROM read_json_auto('{json_file_path}').walls
WHERE 
    bounds = 'EXTERIOR' AND geometry.tilt > 45;
"""

results = con.execute(query).fetchall()

for row in results:
    print(row)

con.close()
