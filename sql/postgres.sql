-- 1. Create a new user (role) for your project with a secure password.
CREATE USER hulc WITH PASSWORD 'hulc123';

-- 2. Create a new database for your project.
CREATE DATABASE hulc_db;

-- Connect to the 'hulc_db' database as the 'hulc' user to perform the following operations.

-- 3. Grant all privileges on the new database to your new user.
-- This allows your user to create tables, insert data, etc., but ONLY in this database.
GRANT ALL PRIVILEGES ON DATABASE hulc_db TO hulc;

GRANT CREATE ON SCHEMA public TO hulc;
GRANT ALL ON SCHEMA public TO hulc;