# %% setup
import os
import json
import sqlite3

def find_cteepbd_files(base_path):
    """
    Finds all DATOS_CTEEPBD.TXT files within the specified base path, case-insensitively.
    """
    cteepbd_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.upper() == "DATOS_CTEEPBD.TXT":
                cteepbd_files.append(os.path.join(root, file))
    return cteepbd_files

def parse_cteepbd_txt(file_path):
    """
    Parses a DATOS_CTEEPBD.TXT file into a structured dictionary.
    It handles metadata, consumption (consumos), and production (produccion) data lines.
    """
    data = {
        "metadata": {},
        "consumos": [],
        "produccion": []
    }
    try:
        with open(file_path, 'r', encoding='latin-1') as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith(';') or line.startswith('__'):
                    continue

                if line.startswith('#META'):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        key = parts[0][5:].strip()
                        value_str = parts[1].strip()
                        try:
                            if ',' in value_str:
                                value = [float(v.strip()) for v in value_str.split(',')]
                            else:
                                value = float(value_str)
                        except (ValueError, TypeError):
                            value = value_str
                        data["metadata"][key] = value
                    continue
                
                if line.startswith('#'):
                    continue

                comment = ''
                if '#' in line:
                    line, comment = line.split('#', 1)
                    line = line.strip()
                    comment = comment.strip()

                parts = [p.strip() for p in line.split(',') if p.strip()]
                if not parts:
                    continue

                values = []
                text_parts = []
                for part in parts:
                    try:
                        values.append(float(part.replace(',', '.')))
                    except ValueError:
                        text_parts.append(part)
                
                if not values:
                    continue

                record = {
                    "descripcion": comment,
                    "fuente": text_parts[0] if text_parts else None,
                    "valores_mensuales": values
                }
                
                record_type_keyword = text_parts[1].upper() if len(text_parts) > 1 else ''

                if record_type_keyword == 'CONSUMO':
                    record["tipo"] = "CONSUMO"
                    if len(text_parts) > 2: record["medida"] = text_parts[2]
                    if len(text_parts) > 3: record["servicio"] = text_parts[3]
                    data["consumos"].append(record)
                elif record_type_keyword == 'PRODUCCION':
                    record["tipo"] = "PRODUCCION"
                    if len(text_parts) > 2: record["modo"] = text_parts[2]
                    if len(text_parts) > 3: record["submodo"] = text_parts[3]
                    data["produccion"].append(record)
                else:
                    if "otros" not in data: data["otros"] = []
                    data["otros"].append(record)

    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

    return data

def save_json_file(data, original_file_path):
    """Saves the parsed data as a JSON file."""
    base_path = os.path.splitext(original_file_path)[0]
    json_file_path = base_path + '.JSON'
    try:
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Saved JSON to {json_file_path}")
    except Exception as e:
        print(f"Error saving JSON to {json_file_path}: {e}")

def save_sqlite_db(data, original_file_path):
    """Saves the parsed data into an SQLite database."""
    base_path = os.path.splitext(original_file_path)[0]
    db_file_path = base_path + '.sqlite'
    
    if os.path.exists(db_file_path):
        os.remove(db_file_path)

    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # Create tables
        cursor.execute('''
        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT
        )''')
        
        cursor.execute('''
        CREATE TABLE consumos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT,
            fuente TEXT,
            medida TEXT,
            servicio TEXT
        )''')

        cursor.execute('''
        CREATE TABLE produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT,
            fuente TEXT,
            modo TEXT,
            submodo TEXT
        )''')

        cursor.execute('''
        CREATE TABLE valores_mensuales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_id INTEGER,
            entry_type TEXT,
            mes INTEGER,
            valor REAL,
            FOREIGN KEY(entry_id) REFERENCES consumos(id),
            FOREIGN KEY(entry_id) REFERENCES produccion(id)
        )''')

        # Insert data
        for key, value in data.get('metadata', {}).items():
            cursor.execute("INSERT INTO metadata VALUES (?, ?)", (key, json.dumps(value)))

        for record in data.get('consumos', []):
            cursor.execute("INSERT INTO consumos (descripcion, fuente, medida, servicio) VALUES (?, ?, ?, ?)",
                           (record.get('descripcion'), record.get('fuente'), record.get('medida'), record.get('servicio')))
            entry_id = cursor.lastrowid
            for i, val in enumerate(record.get('valores_mensuales', [])):
                cursor.execute("INSERT INTO valores_mensuales (entry_id, entry_type, mes, valor) VALUES (?, ?, ?, ?)",
                               (entry_id, 'consumo', i + 1, val))

        for record in data.get('produccion', []):
            cursor.execute("INSERT INTO produccion (descripcion, fuente, modo, submodo) VALUES (?, ?, ?, ?)",
                           (record.get('descripcion'), record.get('fuente'), record.get('modo'), record.get('submodo')))
            entry_id = cursor.lastrowid
            for i, val in enumerate(record.get('valores_mensuales', [])):
                cursor.execute("INSERT INTO valores_mensuales (entry_id, entry_type, mes, valor) VALUES (?, ?, ?, ?)",
                               (entry_id, 'produccion', i + 1, val))

        conn.commit()
        print(f"Saved SQLite DB to {db_file_path}")
    except Exception as e:
        print(f"Error saving SQLite DB to {db_file_path}: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    print(f"Current working directory: {os.getcwd()}")
    
    base_project_path = r'C:\ProyectosCTEyCEE\CTEHE2019\Proyectos'

    if not os.path.isdir(base_project_path):
        print(f"Error: Base path '{base_project_path}' is not a valid directory.")
    else:
        cteepbd_files = find_cteepbd_files(base_project_path)
        print(f"Found {len(cteepbd_files)} DATOS_CTEEPBD.TXT files.")

        for file_path in cteepbd_files:
            print(f"Processing {file_path}...")
            parsed_data = parse_cteepbd_txt(file_path)
            if parsed_data:
                save_json_file(parsed_data, file_path)
                save_sqlite_db(parsed_data, file_path)
            print("-" * 30)
