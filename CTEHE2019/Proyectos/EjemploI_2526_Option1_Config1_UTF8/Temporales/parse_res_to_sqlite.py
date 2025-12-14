
import sqlite3
import json
import os
import re

def create_res_schema(cursor):
    """Creates the database schema for the .res file data."""
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results_zone_by_concept (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        zone_name TEXT,
        concept TEXT,
        heating_pos_kwh_m2 REAL,
        heating_neg_kwh_m2 REAL,
        heating_net_kwh_m2 REAL,
        cooling_pos_kwh_m2 REAL,
        cooling_neg_kwh_m2 REAL,
        cooling_net_kwh_m2 REAL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results_component_loads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        component_name TEXT,
        heating_pos_kwh_m2 REAL,
        heating_neg_kwh_m2 REAL,
        heating_net_kwh_m2 REAL,
        cooling_pos_kwh_m2 REAL,
        cooling_neg_kwh_m2 REAL,
        cooling_net_kwh_m2 REAL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results_building_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT UNIQUE NOT NULL,
        annual_heating_kwh_m2 REAL,
        annual_cooling_kwh_m2 REAL,
        monthly_heating_json TEXT,
        monthly_cooling_json TEXT
    )""")
    
    print("'.res' file schema created or already exists.")

def parse_and_insert(res_file_path, db_file_path, project_name):
    """Parses the .res file and inserts data into the SQLite database."""
    
    try:
        with open(res_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: The file was not found at {res_file_path}")
        return
    except Exception as e:
        print(f"Error reading file with utf-8 encoding: {e}")
        return

    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        create_res_schema(cursor)
        cursor.execute("BEGIN")

        current_section = None
        zone_name = ""

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if "RESULTADOS A NIVEL DE ZONAS" in line:
                current_section = "ZONAS"
                zone_name_line = lines[i+3].strip()
                match = re.search(r'"(.*?)"', zone_name_line)
                if match:
                    zone_name = match.group(1)
                i += 5  # Skip to the line after the zone area
                continue

            if "Numero de Componentes" in line:
                current_section = "COMPONENTES"
                num_components = int(lines[i+1].strip())
                i += 3 # Skip header and go to first data line
                for j in range(num_components):
                    data_line = lines[i+j].strip()
                    parts = [p.strip() for p in data_line.split(',')]
                    component_name = parts[0].strip('"')
                    values = [float(v) for v in parts[1:]]
                    cursor.execute("""
                        INSERT INTO results_component_loads 
                        (project_name, component_name, heating_pos_kwh_m2, heating_neg_kwh_m2, heating_net_kwh_m2, cooling_pos_kwh_m2, cooling_neg_kwh_m2, cooling_net_kwh_m2)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                        (project_name, component_name, *values))
                i += num_components
                current_section = None
                continue

            if "RESULTADOS A NIVEL EDIFICIO" in line:
                current_section = "EDIFICIO"
                annual_line = lines[i+2].strip()
                annual_values = [float(v.strip()) for v in annual_line.split(',')]
                monthly_heating_line = lines[i+4].strip()
                monthly_heating_values = [float(v.strip()) for v in monthly_heating_line.split(',')]
                monthly_cooling_line = lines[i+6].strip()
                monthly_cooling_values = [float(v.strip()) for v in monthly_cooling_line.split(',')]
                
                cursor.execute("""
                    INSERT OR REPLACE INTO results_building_summary 
                    (project_name, annual_heating_kwh_m2, annual_cooling_kwh_m2, monthly_heating_json, monthly_cooling_json)
                    VALUES (?, ?, ?, ?, ?)""",
                    (project_name, annual_values[0], annual_values[1], json.dumps(monthly_heating_values), json.dumps(monthly_cooling_values)))
                
                i += 6 
                current_section = None
                continue

            if current_section == "ZONAS":
                # --- FIX: Skip empty lines, the header, and the TOTAL line ---
                if not line or line.startswith("Concepto") or "TOTAL" in line:
                    if "TOTAL" in line:
                        current_section = None # End of this zone's data
                    i += 1
                    continue
                # -----------------------------------------------------------

                parts = [p.strip() for p in line.split(',')]
                concept = parts[0]
                values = [float(v) for v in parts[1:]]
                cursor.execute("""
                    INSERT INTO results_zone_by_concept 
                    (project_name, zone_name, concept, heating_pos_kwh_m2, heating_neg_kwh_m2, heating_net_kwh_m2, cooling_pos_kwh_m2, cooling_neg_kwh_m2, cooling_net_kwh_m2)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (project_name, zone_name, concept, *values))

            i += 1
        
        conn.commit()
        print(f"Successfully parsed and inserted data for project '{project_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def main():
    res_file_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/NewBDL_O.res'
    db_file_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/NewBDL_O.sqlite'
    
    project_name = os.path.basename(os.path.dirname(res_file_path))
    
    parse_and_insert(res_file_path, db_file_path, project_name)

if __name__ == '__main__':
    main()
