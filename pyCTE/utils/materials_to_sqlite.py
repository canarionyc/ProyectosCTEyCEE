import sqlite3
import re
import os

from ply.yacc import debug_file


def parse_material_entry(lines):
    """Parse a single material entry from the BDCatalogo file."""
    material = {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith('..'):
            break

        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"')

            # Map field names to database columns
            field_map = {
                'THICKNESS': 'THICKNESS',
                'CONDUCTIVITY': 'CONDUCTIVITY',
                'DENSITY': 'DENSITY',
                'SPECIFIC-HEAT': 'SPECIFIC_HEAT',
                'VAPOUR-DIFFUSIVITY-FACTOR': 'VAPOUR_DF',
                'NAME': 'NAME',
                'GROUP': 'GRUPO',
                'IMAGE': 'IMAGE',
                'TYPE': 'TYPE'
            }

            if key in field_map:
                db_key = field_map[key]
                material[db_key] = value

    return material if material else None

def parse_bdc_file(file_path):
    """Parse the BDCatalogo_bdc.txt file and extract all materials."""
    materials = []
    grupos = set()

    with open(file_path, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Look for material definitions
        if '= MATERIAL' in line:
            # Extract material name from quotes
            name_match = re.search(r'"([^"]+)"', line)
            if name_match:
                # Collect lines until '..'
                entry_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('..'):
                    entry_lines.append(lines[i])
                    i += 1

                material = parse_material_entry(entry_lines)
                if material and 'NAME' in material:
                    # Determine TYPE: C for library materials
                    if 'LIBRARY' not in material:
                        material['TYPE'] = 'C'
                    else:
                        material['TYPE'] = 'C'

                    materials.append(material)

                    if 'GRUPO' in material:
                        grupos.add(material['GRUPO'])

        i += 1

    return materials, grupos

def create_database(db_path, ddl_path):
    """Create SQLite database with schema from DDL files."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read and execute DDL files in order
    ddl_files = ['grupo.sql', 'material.sql']

    for ddl_file in ddl_files:
        ddl_file_path = os.path.join(ddl_path, ddl_file)
        if os.path.exists(ddl_file_path):
            with open(ddl_file_path, 'r', encoding='utf-8') as f:
                ddl = f.read()
                # SQLite compatibility adjustments
                ddl = ddl.replace('NUMBER(5, 5)', 'REAL')
                ddl = ddl.replace('constraint PK_', 'constraint PK_temp_')
                ddl = ddl.replace('constraint FK_', 'constraint FK_temp_')
                ddl = ddl.replace('constraint CH_', 'constraint CH_temp_')
                cursor.executescript(ddl)

    conn.commit()
    return conn

def insert_data(conn, materials, grupos):
    """Insert parsed data into the database."""
    cursor = conn.cursor()

    # Insert grupos first
    for grupo in grupos:
        cursor.execute(
            "INSERT OR IGNORE INTO grupo (NAME, TYPE) VALUES (?, 'C')",
            (grupo,)
        )

    # Insert materials
    for material in materials:
        cursor.execute("""
            INSERT OR IGNORE INTO material
            (NAME, THICKNESS, CONDUCTIVITY, DENSITY, SPECIFIC_HEAT,
             VAPOUR_DF, IMAGE, TYPE, GRUPO)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            material.get('NAME'),
            float(material['THICKNESS']) if 'THICKNESS' in material else None,
            float(material['CONDUCTIVITY']) if 'CONDUCTIVITY' in material else None,
            float(material['DENSITY']) if 'DENSITY' in material else None,
            float(material['SPECIFIC_HEAT']) if 'SPECIFIC_HEAT' in material else None,
            float(material['VAPOUR_DF']) if 'VAPOUR_DF' in material else None,
            material.get('IMAGE'),
            material.get('TYPE', 'C'),
            material.get('GRUPO')
        ))

    conn.commit()

if __name__ == '__main__':
    # Define paths
    # bdc_file = 'data/Materials_Catalog/BDCatalogo_bdc.txt'
    bdc_file = r'C:\ProyectosCTEyCEE\CTEHE2019\Proyectos\EjemploI_2526_Option1_Config1\newbdl_o_a.inp'
    # db_file = os.path.splitext(bdc_file)[0] + '.db'
    db_file =
    ddl_dir = 'ddl/main'

    print(f"Parsing {bdc_file}...")
    materials, grupos = parse_bdc_file(bdc_file)
    print(f"Found {len(materials)} materials and {len(grupos)} grupos")

    print(f"Creating database {db_file}...")
    conn = create_database(db_file, ddl_dir)

    print("Inserting data...")
    insert_data(conn, materials, grupos)

    # Verify
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM material")
    material_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM grupo")
    grupo_count = cursor.fetchone()[0]

    print(f"Database created successfully!")
    print(f"  Materials: {material_count}")
    print(f"  Grupos: {grupo_count}")

    conn.close()
