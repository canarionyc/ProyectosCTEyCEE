import os
import psycopg
from dotenv import load_dotenv

def inspect_schema():
    """
    Connects to the PostgreSQL database and prints the schema of all tables in the 'public' schema.
    """
    # --- Load .env file from the project root ---
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv_path = os.path.join(project_root, '.env')
    
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)
    else:
        print(f"Warning: .env file not found at {dotenv_path}. Relying on system environment variables.")
    # ---------------------------------------------

    # Get connection details from environment variables
    db_name = os.getenv("POSTGRES_DB_NAME")
    db_user = os.getenv("POSTGRES_DB_USER")
    db_password = os.getenv("POSTGRES_DB_PASSWORD")
    db_host = os.getenv("POSTGRES_DB_HOST", "localhost")

    if not all([db_name, db_user, db_password]):
        print("Error: Database environment variables (POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD) are not set.")
        return

    conn_string = f"dbname={db_name} user={db_user} password={db_password} host={db_host}"
    
    print(f"\n--- Connecting to database '{db_name}' on host '{db_host}' ---")

    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
                # Query to get table names
                table_query = """
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                ORDER BY table_name;
                """
                cur.execute(table_query)
                tables = cur.fetchall()

                if not tables:
                    print("No tables found in the 'public' schema.")
                    return

                print("\nFound the following tables. Inspecting schema for each:\n")

                # For each table, get its columns and data types
                for table in tables:
                    table_name = table[0]
                    print(f"--- Table: {table_name} ---")
                    
                    column_query = """
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = %s 
                    ORDER BY ordinal_position;
                    """
                    cur.execute(column_query, (table_name,))
                    columns = cur.fetchall()
                    
                    for column in columns:
                        print(f"  - {column[0]} ({column[1]})")
                    print("")

    except psycopg.OperationalError as e:
        print(f"Error: Could not connect to or query the database: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    inspect_schema()
