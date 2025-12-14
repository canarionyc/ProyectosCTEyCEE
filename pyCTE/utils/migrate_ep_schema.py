import sqlite3
import json
import os

def migrate_schema(db_file_path):
    """
    Migrates the schema of the EP database to normalize monthly and annual data.

    This script reads from 'ep_components_data', which is assumed to store
    monthly and annual values in a JSON list, and populates two new tables:
    - ep_monthly_components: with one row per month for each component.
    - ep_annual_components: with one row for each component's annual total.
    """
    if not os.path.exists(db_file_path):
        print(f"Error: Database file not found at '{db_file_path}'")
        return

    print(f"--- Starting schema migration for '{db_file_path}' ---")
    
    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # --- 1. Create the new normalized tables ---
        print("Creating new normalized tables: 'ep_monthly_components' and 'ep_annual_components'...")
        
        # Drop tables if they exist to make the script re-runnable
        cursor.execute("DROP TABLE IF EXISTS ef_monthly_components;")
        cursor.execute("DROP TABLE IF EXISTS ep_annual_components;")

        # Table for normalized monthly data
        cursor.execute("""
        CREATE TABLE ep_monthly_components (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_component_id INTEGER,
            project_name TEXT,
            carrier TEXT,
            service TEXT,
            month_name TEXT,
            month_number INTEGER,
            value REAL,
            FOREIGN KEY(original_component_id) REFERENCES ep_components_data(id)
        );
        """)

        # Table for denormalized annual data
        cursor.execute("""
        CREATE TABLE ep_annual_components (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_component_id INTEGER,
            project_name TEXT,
            carrier TEXT,
            service TEXT,
            annual_value REAL,
            FOREIGN KEY(original_component_id) REFERENCES ep_components_data(id)
        );
        """)
        print("New tables created successfully.")

        # --- 2. Fetch data from the original table ---
        print("Fetching data from 'ep_components_data' and 'ep_meta'...")
        query = """
        SELECT 
            c.id, 
            m.project_name, 
            c.carrier, 
            c.service, 
            c.values_json 
        FROM 
            ep_components_data c
        JOIN 
            ep_meta m ON c.project_id = m.id;
        """
        cursor.execute(query)
        rows_to_migrate = cursor.fetchall()
        print(f"Found {len(rows_to_migrate)} component rows to migrate.")

        # --- 3. Process and insert data into new tables ---
        monthly_rows_inserted = 0
        annual_rows_inserted = 0
        MONTHS = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

        for row in rows_to_migrate:
            component_id, project_name, carrier, service, values_json = row
            
            try:
                values = json.loads(values_json)
                
                # We expect a list of 12 monthly values and optionally a 13th for the annual total
                if isinstance(values, list) and len(values) >= 12:
                    # Insert 12 monthly rows
                    for i in range(12):
                        month_name = MONTHS[i]
                        month_number = i + 1
                        value = values[i]
                        cursor.execute("""
                        INSERT INTO ef_monthly_components 
                            (original_component_id, project_name, carrier, service, month_name, month_number, value)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """, (component_id, project_name, carrier, service, month_name, month_number, value))
                    monthly_rows_inserted += 12

                    # Insert annual row if the data exists (assuming it's the 13th element)
                    if len(values) > 12:
                        annual_value = values[12]
                        cursor.execute("""
                        INSERT INTO ep_annual_components
                            (original_component_id, project_name, carrier, service, annual_value)
                        VALUES (?, ?, ?, ?, ?)
                        """, (component_id, project_name, carrier, service, annual_value))
                        annual_rows_inserted += 1
                else:
                    print(f"  - Warning: Skipping row with component_id {component_id} due to unexpected JSON format.")

            except (json.JSONDecodeError, TypeError) as e:
                print(f"  - Warning: Could not parse JSON for component_id {component_id}. Error: {e}")

        # --- 4. Commit changes ---
        conn.commit()
        print("\nMigration complete.")
        print(f"Total rows inserted into 'ep_monthly_components': {monthly_rows_inserted}")
        print(f"Total rows inserted into 'ep_annual_components': {annual_rows_inserted}")

    except sqlite3.Error as e:
        print(f"\nAn error occurred during the database migration: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
        print("--- Database connection closed ---")

if __name__ == '__main__':
    # The database file path provided by the user
    db_path = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/Temporales/SALIDA_CTEEPBD_EP.sqlite'
    migrate_schema(db_path)
