
import sqlite3
import json
import os

def create_schema(cursor):
    """Creates the database schema."""
    # Main project table from 'meta'
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        is_new_building BOOLEAN,
        climate TEXT,
        num_dwellings INTEGER
    )""")

    # Spaces table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS spaces (
        id TEXT PRIMARY KEY,
        project_id INTEGER,
        name TEXT,
        kind TEXT,
        inside_tenv BOOLEAN,
        height REAL,
        z REAL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )""")

    # Walls table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS walls (
        id TEXT PRIMARY KEY,
        project_id INTEGER,
        space_id TEXT,
        name TEXT,
        bounds TEXT,
        cons_id TEXT,
        next_to_space_id TEXT,
        geometry_json TEXT, -- Store nested geometry object as JSON text
        FOREIGN KEY (project_id) REFERENCES projects (id),
        FOREIGN KEY (space_id) REFERENCES spaces (id)
    )""")
    
    # Windows table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS windows (
        id TEXT PRIMARY KEY,
        project_id INTEGER,
        wall_id TEXT,
        name TEXT,
        cons_id TEXT,
        geometry_json TEXT,
        FOREIGN KEY (project_id) REFERENCES projects (id),
        FOREIGN KEY (wall_id) REFERENCES walls (id)
    )""")

    # Materials table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materials (
        id TEXT PRIMARY KEY,
        project_id INTEGER,
        name TEXT,
        conductivity REAL,
        density REAL,
        specific_heat REAL,
        vapour_diff REAL,
        resistance REAL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    )""")
    print("Schema created or already exists.")

def main():
    json_file_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/envolventecte-6716947208413769375.json'
    db_file_path = 'C:/ProyectosCTEyCEE/SALIDA_CTEEPBD_EP.sqlite'

    # --- Read the JSON file ---
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return

    conn = None
    try:
        # --- Connect to SQLite and set up ---
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        
        # Enable foreign key support
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Create tables if they don't exist
        create_schema(cursor)

        # --- Begin Transaction ---
        cursor.execute("BEGIN")

        # 1. Process 'meta' -> 'projects' table
        meta = data.get('meta', {})
        project_name = meta.get('name')
        if not project_name:
            raise ValueError("Project name not found in JSON meta")

        cursor.execute("INSERT OR IGNORE INTO projects (name, is_new_building, climate, num_dwellings) VALUES (?, ?, ?, ?)",
                       (project_name, meta.get('is_new_building'), meta.get('climate'), meta.get('num_dwellings')))
        
        cursor.execute("SELECT id FROM projects WHERE name = ?", (project_name,))
        project_id_row = cursor.fetchone()
        if not project_id_row:
            raise Exception("Failed to retrieve project_id")
        project_id = project_id_row[0]
        
        print(f"Processing project '{project_name}' with ID: {project_id}")

        # 2. Process 'spaces'
        for space in data.get('spaces', []):
            cursor.execute("INSERT OR IGNORE INTO spaces (id, project_id, name, kind, inside_tenv, height, z) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (space['id'], project_id, space.get('name'), space.get('kind'), space.get('inside_tenv'), space.get('height'), space.get('z')))

        # 3. Process 'walls'
        for wall in data.get('walls', []):
            geometry_str = json.dumps(wall.get('geometry')) if wall.get('geometry') else None
            cursor.execute("INSERT OR IGNORE INTO walls (id, project_id, space_id, name, bounds, cons_id, next_to_space_id, geometry_json) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (wall['id'], project_id, wall.get('space'), wall.get('name'), wall.get('bounds'), wall.get('cons'), wall.get('next_to'), geometry_str))

        # 4. Process 'windows'
        for window in data.get('windows', []):
            geometry_str = json.dumps(window.get('geometry')) if window.get('geometry') else None
            cursor.execute("INSERT OR IGNORE INTO windows (id, project_id, wall_id, name, cons_id, geometry_json) VALUES (?, ?, ?, ?, ?, ?)",
                           (window['id'], project_id, window.get('wall'), window.get('name'), window.get('cons'), geometry_str))

        # 5. Process 'materials'
        for material in data.get('cons', {}).get('materials', []):
             cursor.execute("INSERT OR IGNORE INTO materials (id, project_id, name, conductivity, density, specific_heat, vapour_diff, resistance) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (material['id'], project_id, material.get('name'), material.get('conductivity'), material.get('density'), material.get('specific_heat'), material.get('vapour_diff'), material.get('resistance')))

        # --- Commit Transaction ---
        conn.commit()
        print("Successfully shredded and inserted all data into the relational database.")

    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            print("Rolling back transaction.")
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
