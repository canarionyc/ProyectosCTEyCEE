import os, sys
import pandas as pd
import re
import openpyxl
from pprint import pprint
def safe_float_convert(value):
    """Safely convert string to float, return original if conversion fails"""
    if isinstance(value, str):
        try:
            return float(value)
        except (ValueError, TypeError):
            return value
    return value

def parse_materials_file(filename):
    """
    Parse the materials database file and separate PROPERTIES and RESISTANCE materials
    """
    properties_materials = []
    resistance_materials = []
    current_material = None
    material_type = None
    
    with open(filename, 'r', encoding='iso-8859-1') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('$'):
                continue
            
            # Start of new material definition
            if line.endswith('= MATERIAL'):
                # Save previous material if exists
                if current_material and material_type:
                    if material_type == 'PROPERTIES':
                        properties_materials.append(current_material)
                    elif material_type == 'RESISTANCE':
                        resistance_materials.append(current_material)
                
                # Start new material
                material_name = line.split('=')[0].strip().strip('"')
                current_material = {'NAME': material_name}
                material_type = None
            
            # Property lines
            elif '=' in line and current_material is not None:
                parts = line.split('=', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip().strip('"')
                    
                    # Remove trailing spaces and clean up value
                    value = re.sub(r'\s+', ' ', value).strip()
                    
                    # Track material type
                    if key == 'TYPE':
                        material_type = value
                    
                    # Convert numeric properties to float
                    if key in ['THICKNESS', 'CONDUCTIVITY', 'DENSITY', 'SPECIFIC-HEAT', 
                              'RESISTANCE', 'ABSORPTANCE', 'TRANSMITTANCE', 'EMISSIVITY',
                              'VISCOSITY', 'THERMAL-CAPACITY', 'VAPOUR-DIFFUSION-RESISTANCE-FACTOR',
                              'POROSITY', 'WATER-VAPOUR-DIFFUSION-RESISTANCE', 'REFERENCE-WATER-CONTENT']:
                        current_material[key] = safe_float_convert(value)
                    else:
                        current_material[key] = value
            
            # End of material definition
            elif line == '..':
                if current_material and material_type:
                    if material_type == 'PROPERTIES':
                        properties_materials.append(current_material)
                    elif material_type == 'RESISTANCE':
                        resistance_materials.append(current_material)
                current_material = None
                material_type = None
    
    return properties_materials, resistance_materials

def write_materials_to_excel(properties_materials, resistance_materials, output_filename):
    """
    Write materials to Excel file with separate sheets
    """
    with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
        
        # Write PROPERTIES materials
        if properties_materials:
            df_properties = pd.DataFrame(properties_materials)
            # Reorder columns to put NAME first
            cols = ['NAME'] + [col for col in df_properties.columns if col != 'NAME']
            df_properties = df_properties[cols]

            # Apply additional float conversions for any columns that might have been missed
            numeric_columns = ['THICKNESS', 'CONDUCTIVITY', 'DENSITY', 'SPECIFIC-HEAT', 
                             'RESISTANCE', 'ABSORPTANCE', 'TRANSMITTANCE', 'EMISSIVITY',
                             'VISCOSITY', 'THERMAL-CAPACITY', 'VAPOUR-DIFFUSION-RESISTANCE-FACTOR',
                             'POROSITY', 'WATER-VAPOUR-DIFFUSION-RESISTANCE', 'REFERENCE-WATER-CONTENT']

            for col in numeric_columns:
                if col in df_properties.columns:
                    df_properties[col] = df_properties[col].apply(safe_float_convert)

            df_properties.to_excel(writer, sheet_name='PROPERTIES', index=False)

        # Write RESISTANCE materials  
        if resistance_materials:
            df_resistance = pd.DataFrame(resistance_materials)
            # Reorder columns to put NAME first
            cols = ['NAME'] + [col for col in df_resistance.columns if col != 'NAME']
            df_resistance = df_resistance[cols]

            # Apply additional float conversions for any columns that might have been missed
            numeric_columns = ['THICKNESS', 'CONDUCTIVITY', 'DENSITY', 'SPECIFIC-HEAT', 
                             'RESISTANCE', 'ABSORPTANCE', 'TRANSMITTANCE', 'EMISSIVITY',
                             'VISCOSITY', 'THERMAL-CAPACITY', 'VAPOUR-DIFFUSION-RESISTANCE-FACTOR',
                             'POROSITY', 'WATER-VAPOUR-DIFFUSION-RESISTANCE', 'REFERENCE-WATER-CONTENT']

            for col in numeric_columns:
                if col in df_resistance.columns:
                    df_resistance[col] = df_resistance[col].apply(safe_float_convert)

            df_resistance.to_excel(writer, sheet_name='RESISTANCE', index=False)

if __name__ == "__main__":

    input_file = sys.argv[1] if len(sys.argv) > 1 else r'C:\dev\pyCTE\data\Materials_Catalog\BDCatalogo_bdc.txt'
    output_file =  f"{os.path.splitext(input_file)[0]}_results.xlsx"
    
    try:
        print(f"Parsing materials file '{input_file}'")
        properties_materials, resistance_materials = parse_materials_file(input_file)
        
        print(f"Found {len(properties_materials)} PROPERTIES materials")
        pprint(properties_materials)
        print(f"Found {len(resistance_materials)} RESISTANCE materials")
        
        print("Writing to Excel file...")
        write_materials_to_excel(properties_materials, resistance_materials, output_file)
        
        print(f"Successfully created {output_file}")
        
        # Show some material_item data
        # if properties_materials:
        #     print("\nPROPERTIES material:")
        #     material_item = properties_materials[0]
        #     for key in list(material_item.keys()):  # Show first 5 properties
        #         print(f"  {key}: {material_item[key]}")
        #
        # if resistance_materials:
        #     print("\nRESISTANCE material:")
        #     material_item = resistance_materials[0]
        #     for key in list(material_item.keys()):  # Show first 5 properties
        #         print(f"  {key}: {material_item[key]}")
                
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

