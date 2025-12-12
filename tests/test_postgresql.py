import os
import unittest
import psycopg
from dotenv import load_dotenv

# --- Explicitly load the .env file from the project root ---
# Get the directory of the current script
test_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.dirname(test_dir)
dotenv_path = os.path.join(project_root, '.env')

# Load the .env file from the specified path with verbose output
was_loaded = load_dotenv(dotenv_path=dotenv_path, verbose=True)

if not was_loaded:
    print(f"Warning: .env file not found at {dotenv_path}. Relying on system environment variables.")
# ----------------------------------------------------------------

class TestPostgreSQLConnection(unittest.TestCase):
    """
    Test suite for verifying PostgreSQL database connectivity and basic operations.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the database connection details from environment variables once for the entire test class.
        """
        cls.DB_NAME = os.getenv("POSTGRES_DB_NAME")
        cls.DB_USER = os.getenv("POSTGRES_DB_USER")
        cls.DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD")
        cls.DB_HOST = os.getenv("POSTGRES_DB_HOST", "localhost")

        # Ensure all required environment variables are set before running tests
        if not all([cls.DB_NAME, cls.DB_USER, cls.DB_PASSWORD]):
            raise unittest.SkipTest(
                "Database environment variables (POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD) are not set. Skipping tests."
            )

        cls.conn_string = f"dbname={cls.DB_NAME} user={cls.DB_USER} password={cls.DB_PASSWORD} host={cls.DB_HOST}"

    def test_database_connection(self):
        """
        Tests if a connection to the PostgreSQL database can be successfully established.
        """
        try:
            with psycopg.connect(self.conn_string) as conn:
                self.assertIsNotNone(conn, "Connection object should not be None.")
        except psycopg.OperationalError as e:
            self.fail(f"Could not connect to the database: {e}")

    def test_fetch_postgresql_version(self):
        """
        Tests that the PostgreSQL version can be successfully fetched.
        """
        try:
            with psycopg.connect(self.conn_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT version();")
                    db_version = cur.fetchone()
                    
                    self.assertIsNotNone(db_version, "Fetching version should return a result.")
                    self.assertTrue(isinstance(db_version[0], str), "Version should be a string.")
                    self.assertIn("PostgreSQL", db_version[0], "Result should contain 'PostgreSQL'.")
        except psycopg.OperationalError as e:
            self.fail(f"Database operation failed: {e}")

    def test_list_tables_in_public_schema(self):
        """
        Connects to the database and lists all tables in the 'public' schema.
        """
        print("\n--- Attempting to list tables in 'public' schema ---")
        try:
            with psycopg.connect(self.conn_string) as conn:
                with conn.cursor() as cur:
                    # Query to get table names from the information_schema
                    query = """
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    ORDER BY table_name;
                    """
                    cur.execute(query)
                    tables = cur.fetchall()

                    self.assertIsNotNone(tables, "Query should return a result, even if empty.")
                    
                    if not tables:
                        print("No tables found in the 'public' schema.")
                    else:
                        print("Found the following tables:")
                        for table in tables:
                            print(f"- {table[0]}")
                    
                    # This makes it a true test: we expect at least one table
                    self.assertTrue(len(tables) > 0, "Should find at least one table in the public schema.")

        except psycopg.OperationalError as e:
            self.fail(f"Database operation failed while trying to list tables: {e}")

if __name__ == '__main__':
    unittest.main()
