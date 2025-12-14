
import sqlite3
import json
import os

def create_ep_schema(cursor):
    """Creates the normalized database schema for the EP (Energy Performance) JSON data."""
    
    # --- Main Metadata Table ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ep_meta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT UNIQUE NOT NULL,
        k_exp REAL,
        arearef REAL,
        fraccion_renovable_demanda_acs_nrb REAL,
        demanda_anual_acs REAL
    )""")

    # --- Normalized Monthly and Annual Data Tables ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ep_monthly_components (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        carrier TEXT,
        ctype TEXT,
        csubtype TEXT,
        service TEXT,
        month_name TEXT,
        month_number INTEGER,
        value REAL,
        comment TEXT,
        FOREIGN KEY (project_id) REFERENCES ep_meta (id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ep_annual_components (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        carrier TEXT,
        ctype TEXT,
        csubtype TEXT,
        service TEXT,
        annual_value REAL,
        comment TEXT,
        FOREIGN KEY (project_id) REFERENCES ep_meta (id)
    )""")

    # --- Other Tables ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ep_components_meta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        key TEXT,
        value TEXT,
        FOREIGN KEY (project_id) REFERENCES ep_meta (id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ep_weight_factors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        carrier TEXT,
        source TEXT,
        dest TEXT,
        step TEXT,
        ren REAL,
        nren REAL,
        co2 REAL,
        comment TEXT,
        FOREIGN KEY (project_id) REFERENCES ep_meta (id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ep_balance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        carrier TEXT,
        balance_json TEXT,
        FOREIGN KEY (project_id) REFERENCES ep_meta (id)
    )""")

    print("Normalized EP schema created or already exists.")

def main():
    project_name = "EjemploI_2526_Option1_Config1" 
    json_file_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/Temporales/SALIDA_CTEEPBD_EP.JSON'
    db_file_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/Temporales/SALIDA_CTEEPBD_EP.sqlite'

    if os.path.exists(db_file_path):
        os.remove(db_file_path)
        print(f"Removed existing database file: {db_file_path}")

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return

    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        create_ep_schema(cursor)
        cursor.execute("BEGIN")

        # 1. Process 'ep_meta'
        misc_data = data.get('misc', {})
        cursor.execute("INSERT INTO ep_meta (project_name, k_exp, arearef, fraccion_renovable_demanda_acs_nrb, demanda_anual_acs) VALUES (?, ?, ?, ?, ?)",
                       (project_name, data.get('k_exp'), data.get('arearef'), misc_data.get('fraccion_renovable_demanda_acs_nrb'), misc_data.get('demanda_anual_acs')))
        project_id = cursor.lastrowid
        print(f"Processing EP data for project '{project_name}' with ID: {project_id}")

        # 2. Process 'components.cmeta'
        for item in data.get('components', {}).get('cmeta', []):
            cursor.execute("INSERT INTO ep_components_meta (project_id, key, value) VALUES (?, ?, ?)",
                           (project_id, item.get('key'), item.get('value')))

        # 3. Process 'components.cdata' into NORMALIZED tables
        MONTHS = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        for item in data.get('components', {}).get('cdata', []):
            values = item.get('values', [])
            if not (isinstance(values, list) and len(values) >= 12):
                continue

            # Insert 12 monthly rows
            for i in range(12):
                cursor.execute("""
                INSERT INTO ef_monthly_components (project_id, carrier, ctype, csubtype, service, month_name, month_number, value, comment) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                               (project_id, item.get('carrier'), item.get('ctype'), item.get('csubtype'), item.get('service'), MONTHS[i], i + 1, values[i], item.get('comment')))

            # --- FIX: Calculate the annual total from the monthly values ---
            annual_value = sum(values[:12])
            cursor.execute("""
            INSERT INTO ep_annual_components (project_id, carrier, ctype, csubtype, service, annual_value, comment) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (project_id, item.get('carrier'), item.get('ctype'), item.get('csubtype'), item.get('service'), annual_value, item.get('comment')))

        # 4. Process 'wfactors.wdata'
        for item in data.get('wfactors', {}).get('wdata', []):
            cursor.execute("INSERT INTO ep_weight_factors (project_id, carrier, source, dest, step, ren, nren, co2, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (project_id, item.get('carrier'), item.get('source'), item.get('dest'), item.get('step'), item.get('ren'), item.get('nren'), item.get('co2'), item.get('comment')))

        # 5. Process 'balance_cr'
        for carrier, balance_data in data.get('balance_cr', {}).items():
            balance_str = json.dumps(balance_data)
            cursor.execute("INSERT INTO ep_balance (project_id, carrier, balance_json) VALUES (?, ?, ?)",
                           (project_id, carrier, balance_str))

        conn.commit()
        print("Successfully shredded and inserted EP JSON data into the normalized database.")

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
