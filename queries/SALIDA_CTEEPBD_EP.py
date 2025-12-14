import sqlite3
import json
# Define the paths for the JSON and SQLite files
json_file_path = r"C:\ProyectosCTEyCEE\CTEHE2019\Proyectos\EjemploI_2526_Option1_Config1\Temporales\SALIDA_CTEEPBD_EP.JSON"
db_file_path = r"C:\ProyectosCTEyCEE\CTEHE2019\Proyectos\EjemploI_2526_Option1_Config1\Temporales\SALIDA_CTEEPBD_EP.sqlite"

# --- Read the JSON file content ---
with open(json_file_path, 'r', encoding='utf-8') as f:
    json_content_string = f.read()
    # You can also load it into a dictionary if you want to process it first
    # data = json.load(f) 

# --- Connect to SQLite and insert the data ---
try:
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Create a table to hold the raw JSON data
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS raw_json_data
                   (
                       id           INTEGER PRIMARY KEY,
                       project_name TEXT,
                       json_text    TEXT
                   )
    ''')

    # For this example, let's extract the project name and store the whole file
    data = json.loads(json_content_string)
    project_name = data.get('meta', {}).get('name', 'unknown')

    # Insert the JSON content into the table
    cursor.execute("INSERT INTO raw_json_data (project_name, json_text) VALUES (?, ?)",
                   (project_name, json_content_string))

    conn.commit()
    print(f"Successfully inserted data for project '{project_name}' into the database.")

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
