
import xml.etree.ElementTree as ET
import duckdb
import pandas as pd

def get_text(element, path, default=''):
    """Safely get text from an XML element."""
    node = element.find(path)
    return node.text if node is not None else default

def main():
    xml_file = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/Temporales/ejemploi_2526_option1_config1.xml'
    db_file = 'C:/ProyectosCTEyCEE/CTEHE2019/Proyectos/EjemploI_2526_Option1_Config1/Temporales/building_data.duckdb'

    # Connect to DuckDB
    con = duckdb.connect(database=db_file, read_only=False)

    # Parse XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # --- Create and populate tables ---
    
    # DatosDelCertificador
    certificador = root.find('DatosDelCertificador')
    if certificador is not None:
        df_certificador = pd.DataFrame([{
            'NombreyApellidos': get_text(certificador, 'NombreyApellidos'),
            'NIF': get_text(certificador, 'NIF'),
            'RazonSocial': get_text(certificador, 'RazonSocial'),
            'Fecha': get_text(certificador, 'Fecha'),
        }])
        con.execute("CREATE OR REPLACE TABLE DatosDelCertificador AS SELECT * FROM df_certificador")

    # IdentificacionEdificio
    identificacion = root.find('IdentificacionEdificio')
    if identificacion is not None:
        df_identificacion = pd.DataFrame([{
            'NombreDelEdificio': get_text(identificacion, 'NombreDelEdificio'),
            'ZonaClimatica': get_text(identificacion, 'ZonaClimatica'),
            'TipoDeEdificio': get_text(identificacion, 'TipoDeEdificio'),
            'NormativaVigente': get_text(identificacion, 'NormativaVigente'),
        }])
        con.execute("CREATE OR REPLACE TABLE IdentificacionEdificio AS SELECT * FROM df_identificacion")

    # DatosGeneralesyGeometria
    geometria = root.find('DatosGeneralesyGeometria')
    if geometria is not None:
        df_geometria = pd.DataFrame([{
            'SuperficieHabitable': float(get_text(geometria, 'SuperficieHabitable', 0)),
            'VolumenEspacioHabitable': float(get_text(geometria, 'VolumenEspacioHabitable', 0)),
            'Compacidad': float(get_text(geometria, 'Compacidad', 0)),
        }])
        con.execute("CREATE OR REPLACE TABLE DatosGeneralesyGeometria AS SELECT * FROM df_geometria")

    # PuentesTermicos
    puentes_termicos = root.find('DatosEnvolventeTermica/PuentesTermicos')
    if puentes_termicos is not None:
        puentes_data = []
        for elem in puentes_termicos.findall('Elemento'):
            puentes_data.append({
                'Nombre': get_text(elem, 'Nombre'),
                'Tipo': get_text(elem, 'Tipo'),
                'Longitud': float(get_text(elem, 'Longitud', 0)),
                'Transmitancia': float(get_text(elem, 'Transmitancia', 0)),
            })
        if puentes_data:
            df_puentes = pd.DataFrame(puentes_data)
            con.execute("CREATE OR REPLACE TABLE PuentesTermicos AS SELECT * FROM df_puentes")

    # CerramientosOpacos
    cerramientos = root.find('DatosEnvolventeTermica/CerramientosOpacos')
    if cerramientos is not None:
        cerramientos_data = []
        for elem in cerramientos.findall('Elemento'):
            cerramientos_data.append({
                'Nombre': get_text(elem, 'Nombre'),
                'Tipo': get_text(elem, 'Tipo'),
                'Superficie': float(get_text(elem, 'Superficie', 0)),
                'Transmitancia': float(get_text(elem, 'Transmitancia', 0)),
            })
        if cerramientos_data:
            df_cerramientos = pd.DataFrame(cerramientos_data)
            con.execute("CREATE OR REPLACE TABLE CerramientosOpacos AS SELECT * FROM df_cerramientos")

    # HuecosyLucernarios
    huecos = root.find('DatosEnvolventeTermica/HuecosyLucernarios')
    if huecos is not None:
        huecos_data = []
        for elem in huecos.findall('Elemento'):
            huecos_data.append({
                'Nombre': get_text(elem, 'Nombre'),
                'Tipo': get_text(elem, 'Tipo'),
                'Superficie': float(get_text(elem, 'Superficie', 0)),
                'Transmitancia': float(get_text(elem, 'Transmitancia', 0)),
                'FactorSolar': float(get_text(elem, 'FactorSolar', 0)),
            })
        if huecos_data:
            df_huecos = pd.DataFrame(huecos_data)
            con.execute("CREATE OR REPLACE TABLE HuecosyLucernarios AS SELECT * FROM df_huecos")

    print("Database 'building_data.duckdb' created and populated successfully.")
    
    # --- Print final database statistics ---
    print("\n--- Database Stats ---")
    tables_to_check = [
        "DatosDelCertificador",
        "IdentificacionEdificio",
        "DatosGeneralesyGeometria",
        "PuentesTermicos",
        "CerramientosOpacos",
        "HuecosyLucernarios"
    ]
    
    all_tables_in_db = con.execute("SHOW TABLES").fetchdf()['name'].tolist()

    for table_name in tables_to_check:
        if table_name in all_tables_in_db:
            try:
                row_count = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
                print(f"Total rows in {table_name}: {row_count}")
            except duckdb.Error as e:
                print(f"Could not get stats for {table_name}: {e}")
        else:
            print(f"Table {table_name} was not created (no data).")
            
    print("----------------------")

    con.close()

if __name__ == '__main__':
    main()
