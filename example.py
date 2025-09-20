#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example usage of the European Energy Certification XML Parser
"""

import os
import json
from xml_parser import parse_energy_certificate_xml

#%% Example usage
def example_parse_and_display(xml_file_path):
    """
    Parse an XML file and display its JSON representation
    
    Args:
        xml_file_path: Path to the XML file to parse
    """
    print(f"Parsing: {xml_file_path}")
    
    # Parse XML to dictionary
    result = parse_energy_certificate_xml(xml_file_path)
    from pprint import pprint
    pprint(result)
    cte_he=result['CTE-HE-XML']
    datosGenerales=cte_he['DatosGenerales']
    valoresMensualesELE=datosGenerales[ 'valoresMensualesELE']
    print(valoresMensualesELE)
    print(cte_he.keys())

    entradaGraficaLIDER=cte_he['EntradaGraficaLIDER']
    print(entradaGraficaLIDER)

    definicion_Sistema=cte_he['Definicion_Sistema']
    print(definicion_Sistema)

    definicion_Sistema_GT=cte_he['Definicion_Sistema_GT']
    print(definicion_Sistema_GT[0]['Definicion_Sistema_CALENER_GT'])
    print(definicion_Sistema_GT[1]['Definicion_Sistema_CALENER_GT'])

    # Convert to JSON with pretty formatting
    json_output = json.dumps(result, indent=4, ensure_ascii=False)
    
    # Print the JSON
    print("\nJSON Representation:")
    print(json_output)
    
    # Save to a file
    output_path = os.path.splitext(xml_file_path)[0] + ".json"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_output)
    print(f"\nJSON saved to: {output_path}")

#%% Main function
if __name__ == "__main__":
    # You can replace this with an actual XML file path
    # sample_xml_path = "sample_data/energy_certificate.xml"
    sample_xml_path = r'C:\ProyectosCTEyCEE\CTEHE2019\Proyectos\ejemploGT\ejemploGT.ctehexml'
    
    if os.path.exists(sample_xml_path):
        example_parse_and_display(sample_xml_path)
    else:
        print(f"Sample file not found: {sample_xml_path}")
        print("Please provide a valid XML file path as an argument.")
