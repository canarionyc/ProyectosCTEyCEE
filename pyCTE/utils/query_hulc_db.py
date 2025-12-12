# %% setup
import numpy as np
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

import psycopg

load_dotenv()
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")

# Ensure all required environment variables are set before running tests
if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    raise (
        "Database environment variables (POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD) are not set. Skipping tests."
    )

conn_string = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST}"

# Connection details - replace with your actual credentials
# For your application, use the dedicated user you created, not the 'postgres' superuser.
conn_string = "dbname=my_project_db user=my_project_user password=a_very_strong_password host=localhost"

try:
    # Connect to the database
    with psycopg.connect(conn_string) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Execute a query
            cur.execute("SELECT version();")

            # Fetch the result
            db_version = cur.fetchone()
            print(f"Successfully connected to: {db_version[0]}")

except psycopg.OperationalError as e:
    print(f"Could not connect to the database: {e}")

