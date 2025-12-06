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

def parse_layers_entry(lines):
    """Parse a LAYERS (cerramiento) entry."""
    layers = {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith('..'):
            break

        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()

            if key == 'MATERIAL':
                # Parse tuple of materials
                materials_match = re.findall(r'"([^"]+)"', value)
                layers['MATERIALS'] = materials_match
            elif key == 'THICKNESS':
                # Parse tuple of thicknesses
                thicknesses = re.findall(r'[\d.]+', value)
                layers['THICKNESSES'] = [float(t) for t in thicknesses]

    return layers if layers else None

def parse_glass_entry(lines):
    """Parse a GLASS-TYPE (vidrio) entry."""
    glass = {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith('..'):
            break

        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"')

            if key == 'GROUP':
                glass['GRUPO'] = value
            elif key == 'SHADING-COEF':
                glass['FACTORSOLAR'] = value
            elif key == 'GLASS-CONDUCTANCE':
                glass['UVIDRIO'] = value

    return glass if glass else None

def parse_frame_entry(lines):
    """Parse a NAME-FRAME (marco) entry."""
    frame = {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith('..'):
            break

        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"')

            if key == 'GROUP':
                frame['GRUPO'] = value
            elif key == 'FRAME-ABS':
                frame['ABSORTIVIDAD'] = value
            elif key == 'FRAME-CONDUCT':
                frame['UMARCO'] = value

    return frame if frame else None

def parse_bdc_file(file_path):
    """Parse the BDCatalogo_bdc.txt file and extract all materials, cerramientos, vidrios, and marcos."""
    materials = []
    cerramientos = []
    compones = []
    vidrios = []
    marcos = []
    grupos = set()
    gruposVidrio = set()
    gruposMarco = set()

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
                material_name = name_match.group(1)
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

        # Look for LAYERS (cerramiento) definitions - skip names starting with "I_"
        elif '= LAYERS' in line:
            # Extract cerramiento name from quotes
            name_match = re.search(r'"([^"]+)"', line)
            if name_match:
                cerr_name = name_match.group(1)

                # Skip entries starting with "I_"
                if cerr_name.startswith('I_'):
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith('..'):
                        i += 1
                else:
                    # Collect lines until '..'
                    entry_lines = []
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith('..'):
                        entry_lines.append(lines[i])
                        i += 1

                    layers = parse_layers_entry(entry_lines)
                    if layers and 'MATERIALS' in layers:
                        # Create cerramiento entry
                        cerramiento = {'NAME': cerr_name}
                        cerramientos.append(cerramiento)

                        # Create compone entries for each layer
                        materials_list = layers['MATERIALS']
                        thicknesses_list = layers.get('THICKNESSES', [])

                        for orden, (mat_name, thickness) in enumerate(zip(materials_list, thicknesses_list), start=1):
                            compone = {
                                'NAME_CERR': cerr_name,
                                'NAME_MAT': mat_name,
                                'ORDEN': orden,
                                'THICKNESS': thickness
                            }
                            compones.append(compone)

        # Look for GLASS-TYPE (vidrio) definitions
        elif '= GLASS-TYPE' in line:
            # Extract vidrio name from quotes
            name_match = re.search(r'"([^"]+)"', line)
            if name_match:
                vidrio_name = name_match.group(1)
                # Collect lines until '..'
                entry_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('..'):
                    entry_lines.append(lines[i])
                    i += 1

                glass = parse_glass_entry(entry_lines)
                if glass:
                    glass['NAME'] = vidrio_name
                    glass['TYPE'] = 'C'
                    vidrios.append(glass)

                    if 'GRUPO' in glass:
                        gruposVidrio.add(glass['GRUPO'])

        # Look for NAME-FRAME (marco) definitions
        elif '= NAME-FRAME' in line:
            # Extract marco name from quotes
            name_match = re.search(r'"([^"]+)"', line)
            if name_match:
                marco_name = name_match.group(1)
                # Collect lines until '..'
                entry_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('..'):
                    entry_lines.append(lines[i])
                    i += 1

                frame = parse_frame_entry(entry_lines)
                if frame:
                    frame['NAME'] = marco_name
                    frame['TYPE'] = 'C'
                    marcos.append(frame)

                    if 'GRUPO' in frame:
                        gruposMarco.add(frame['GRUPO'])

        i += 1

    return materials, cerramientos, compones, vidrios, marcos, grupos, gruposVidrio, gruposMarco

def create_database(db_path, ddl_path):
    """Create SQLite database with schema from DDL files."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read and execute DDL files in order
    ddl_files = ['grupo.sql', 'material.sql', 'cerramiento.sql', 'compone.sql',
                 'grupoVidrio.sql', 'vidrio.sql', 'grupoMarco.sql', 'marco.sql']

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

def insert_data(conn, materials, cerramientos, compones, vidrios, marcos, grupos, gruposVidrio, gruposMarco):
    """Insert parsed data into the database."""
    cursor = conn.cursor()

    # Insert grupos first
    for grupo in grupos:
        cursor.execute(
            "INSERT OR IGNORE INTO grupo (NAME, TYPE) VALUES (?, 'C')",
            (grupo,)
        )

    # Insert gruposVidrio
    for grupo in gruposVidrio:
        cursor.execute(
            "INSERT OR IGNORE INTO grupoVidrio (NAME, TYPE) VALUES (?, 'C')",
            (grupo,)
        )

    # Insert gruposMarco
    for grupo in gruposMarco:
        cursor.execute(
            "INSERT OR IGNORE INTO grupoMarco (NAME, TYPE) VALUES (?, 'C')",
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

    # Insert cerramientos
    for cerramiento in cerramientos:
        cursor.execute("""
            INSERT OR IGNORE INTO cerramiento (NAME, TRANS_TERMICA, PESOM2)
            VALUES (?, NULL, NULL)
        """, (cerramiento['NAME'],))

    # Insert compones
    for compone in compones:
        cursor.execute("""
            INSERT OR IGNORE INTO compone
            (NAME_CERR, NAME_MAT, ORDEN, THICKNESS)
            VALUES (?, ?, ?, ?)
        """, (
            compone['NAME_CERR'],
            compone['NAME_MAT'],
            compone['ORDEN'],
            compone['THICKNESS']
        ))

    # Insert vidrios
    for vidrio in vidrios:
        cursor.execute("""
            INSERT OR IGNORE INTO vidrio
            (NAME, GRUPO, FACTORSOLAR, UVIDRIO, TYPE)
            VALUES (?, ?, ?, ?, ?)
        """, (
            vidrio.get('NAME'),
            vidrio.get('GRUPO'),
            float(vidrio['FACTORSOLAR']) if 'FACTORSOLAR' in vidrio else None,
            float(vidrio['UVIDRIO']) if 'UVIDRIO' in vidrio else None,
            vidrio.get('TYPE', 'C')
        ))

    # Insert marcos
    for marco in marcos:
        cursor.execute("""
            INSERT OR IGNORE INTO marco
            (NAME, GRUPO, ABSORTIVIDAD, UMARCO, TYPE)
            VALUES (?, ?, ?, ?, ?)
        """, (
            marco.get('NAME'),
            marco.get('GRUPO'),
            float(marco['ABSORTIVIDAD']) if 'ABSORTIVIDAD' in marco else None,
            float(marco['UMARCO']) if 'UMARCO' in marco else None,
            marco.get('TYPE', 'C')
        ))

    conn.commit()

if __name__ == '__main__':
    # Define paths
    # bdc_file = 'data/Materials_Catalog/BDCatalogo_bdc.txt'
    bdc_file = r'C:\ProyectosCTEyCEE\CTEHE2019\Proyectos\EjemploI_2526_Option1_Config1\newbdl_o_a.inp'
    db_file = os.path.join(os.path.dirname(bdc_file), 'bbdd.dat')
    ddl_dir = 'ddl/main'

    print(f"Parsing {bdc_file}...")
    materials, cerramientos, compones, vidrios, marcos, grupos, gruposVidrio, gruposMarco = parse_bdc_file(bdc_file)
    print(f"Found {len(materials)} materials, {len(cerramientos)} cerramientos, {len(compones)} compones, "
          f"{len(vidrios)} vidrios, {len(marcos)} marcos")
    print(f"Groups: {len(grupos)} material grupos, {len(gruposVidrio)} vidrio grupos, {len(gruposMarco)} marco grupos")

    print(f"Creating database {db_file}...")
    conn = create_database(db_file, ddl_dir)

    print("Inserting data...")
    insert_data(conn, materials, cerramientos, compones, vidrios, marcos, grupos, gruposVidrio, gruposMarco)

    # Verify
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM material")
    material_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM grupo")
    grupo_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM cerramiento")
    cerramiento_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM compone")
    compone_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM vidrio")
    vidrio_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM marco")
    marco_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM grupoVidrio")
    grupo_vidrio_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM grupoMarco")
    grupo_marco_count = cursor.fetchone()[0]

    print(f"Database created successfully!")
    print(f"  Materials: {material_count}")
    print(f"  Grupos: {grupo_count}")
    print(f"  Cerramientos: {cerramiento_count}")
    print(f"  Compones: {compone_count}")
    print(f"  Vidrios: {vidrio_count}")
    print(f"  Marcos: {marco_count}")
    print(f"  Grupo Vidrios: {grupo_vidrio_count}")
    print(f"  Grupo Marcos: {grupo_marco_count}")

    conn.close()
