import os
import sqlite3
import duckdb

def find_sqlite_files(base_path):
    """Finds all DATOS_CTEEPBD.sqlite files."""
    sqlite_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == "DATOS_CTEEPBD.sqlite":
                sqlite_files.append(os.path.join(root, file))
    return sqlite_files

def get_project_name(file_path, base_path):
    """Extracts the project directory name from the file path."""
    relative_dir_path = os.path.relpath(os.path.dirname(file_path), base_path)
    project_name = relative_dir_path.split(os.sep)[0]
    return project_name

def run_consolidation():
    base_project_path = r'C:\ProyectosCTEyCEE\CTEHE2019\Proyectos'
    consolidated_db_path = r'C:\ProyectosCTEyCEE\consolidated_results.duckdb'

    query = """
    SELECT
        c.servicio,
        ROUND(SUM(vm.valor) / CAST(json_extract(m.value, '$') AS REAL), 2) AS 'kWh/m2'
    FROM
        consumos c
    JOIN
        valores_mensuales vm ON c.id = vm.entry_id AND vm.entry_type = 'consumo'
    CROSS JOIN
        metadata m
    WHERE
        m.key = 'CTE_AREAREF'
    GROUP BY
        c.servicio;
    """

    # Connect to the consolidated DuckDB database
    consolidated_conn = duckdb.connect(database=consolidated_db_path, read_only=False)
    
    # Create the results table if it doesn't exist
    consolidated_conn.execute('''
    CREATE TABLE IF NOT EXISTS consolidated_consumption (
        proyecto TEXT,
        servicio TEXT,
        kwh_per_m2 REAL,
        PRIMARY KEY (proyecto, servicio)
    )''')

    # Find and process individual sqlite files
    sqlite_files = find_sqlite_files(base_project_path)
    print(f"Found {len(sqlite_files)} SQLite files to process.")

    for db_path in sqlite_files:
        project_name = get_project_name(db_path, base_project_path)
        print(f"Querying data from project: '{project_name}'...")

        individual_conn = None
        try:
            individual_conn = sqlite3.connect(f'file:{db_path}?mode=ro', uri=True)
            results = individual_conn.execute(query).fetchall()

            if results:
                data_to_upsert = [(project_name, row[0], row[1]) for row in results]
                upsert_sql = """
                INSERT INTO consolidated_consumption (proyecto, servicio, kwh_per_m2)
                VALUES (?, ?, ?)
                ON CONFLICT (proyecto, servicio) DO UPDATE SET kwh_per_m2 = excluded.kwh_per_m2;
                """
                consolidated_conn.executemany(upsert_sql, data_to_upsert)
                print(f"  -> Upserted {len(results)} rows for '{project_name}'.")
            else:
                print(f"  -> No results found for '{project_name}'.")

        except sqlite3.Error as e:
            print(f"  -> Error processing {db_path}: {e}")
        finally:
            if individual_conn:
                individual_conn.close()
    
    print("-" * 30)
    print("Consolidation complete.")
    
    # Print final database statistics
    try:
        total_rows = consolidated_conn.execute("SELECT COUNT(*) FROM consolidated_consumption").fetchone()[0]
        total_projects = consolidated_conn.execute("SELECT COUNT(DISTINCT proyecto) FROM consolidated_consumption").fetchone()[0]
        
        print("\n--- Database Stats ---")
        print(f"Total rows in consolidated_consumption: {total_rows}")
        print(f"Total unique projects: {total_projects}")
        print("----------------------")

    except duckdb.Error as e:
        print(f"Could not retrieve stats from the database: {e}")
    finally:
        consolidated_conn.close()
        print(f"Results are in '{consolidated_db_path}'")

if __name__ == '__main__':
    run_consolidation()
