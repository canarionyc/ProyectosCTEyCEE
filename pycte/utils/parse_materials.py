import os, sys
import pandas as pd
import re
import openpyxl
from pprint import pprint

def process_directory(input_dir):
    """Process all *.ctehebdc files in a directory"""
    import glob

    # Find all .ctehebdc files in the directory
    pattern = os.path.join(input_dir, "*_bdc.txt")
    bdc_files = glob.glob(pattern)

    if not bdc_files:
        print(f"No *.ctehebdc files found in directory: {input_dir}")
        return

    print(f"Found {len(bdc_files)} *.bdc files in directory: {input_dir}")

    for bdc_file in bdc_files:
        try:
            process_bdc_file(bdc_file)
        except Exception as e:
            print(f"Error processing {bdc_file}: {str(e)}")
            continue
		    
def safe_float_convert(value):
    """Safely convert string to float, return original if conversion fails"""
    if isinstance(value, str):
        try:
            return float(value)
        except (ValueError, TypeError):
            return value
    return value

def process_bdc_file(input_file):
    """
    Parse a BDC file containing materials, layers, glass types, frames, and gaps.
    Creates an Excel file with separate sheets for each entity type.
    """
    materials_properties = []
    materials_resistance = []
    layers = []
    glass_types = []
    frames = []
    gaps = []

    current_entity = None
    entity_type = None
    material_subtype = None

    with open(input_file, 'r', encoding='iso-8859-1') as f:
        for line in f:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('$'):
                continue

            # Start of new entity definition
            if '= MATERIAL' in line:
                # Save previous material if exists
                if current_entity and entity_type == 'MATERIAL' and material_subtype:
                    if material_subtype == 'PROPERTIES':
                        materials_properties.append(current_entity)
                    elif material_subtype == 'RESISTANCE':
                        materials_resistance.append(current_entity)

                # Start new material
                entity_name = line.split('=')[0].strip().strip('"')
                current_entity = {'NAME': entity_name}
                entity_type = 'MATERIAL'
                material_subtype = None

            elif '= LAYERS' in line:
                # Save previous entity if exists
                if current_entity and entity_type:
                    save_entity(current_entity, entity_type, material_subtype,
                              materials_properties, materials_resistance, layers,
                              glass_types, frames, gaps)

                # Start new layer
                entity_name = line.split('=')[0].strip().strip('"')
                current_entity = {'NAME': entity_name}
                entity_type = 'LAYERS'
                material_subtype = None

            elif '= GLASS-TYPE' in line:
                # Save previous entity if exists
                if current_entity and entity_type:
                    save_entity(current_entity, entity_type, material_subtype,
                              materials_properties, materials_resistance, layers,
                              glass_types, frames, gaps)

                # Start new glass type
                entity_name = line.split('=')[0].strip().strip('"')
                current_entity = {'NAME': entity_name}
                entity_type = 'GLASS-TYPE'
                material_subtype = None

            elif '= NAME-FRAME' in line:
                # Save previous entity if exists
                if current_entity and entity_type:
                    save_entity(current_entity, entity_type, material_subtype,
                              materials_properties, materials_resistance, layers,
                              glass_types, frames, gaps)

                # Start new frame
                entity_name = line.split('=')[0].strip().strip('"')
                current_entity = {'NAME': entity_name}
                entity_type = 'NAME-FRAME'
                material_subtype = None

            elif '= GAP' in line:
                # Save previous entity if exists
                if current_entity and entity_type:
                    save_entity(current_entity, entity_type, material_subtype,
                              materials_properties, materials_resistance, layers,
                              glass_types, frames, gaps)

                # Start new gap
                entity_name = line.split('=')[0].strip().strip('"')
                current_entity = {'NAME': entity_name}
                entity_type = 'GAP'
                material_subtype = None

            # Property lines
            elif '=' in line and current_entity is not None:
                parts = line.split('=', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip().strip('"')

                    # Remove trailing spaces and clean up value
                    value = re.sub(r'\s+', ' ', value).strip()

                    # Track material subtype
                    if key == 'TYPE' and entity_type == 'MATERIAL':
                        material_subtype = value

                    # Convert numeric properties to float
                    numeric_keys = [
                        'THICKNESS', 'CONDUCTIVITY', 'DENSITY', 'SPECIFIC-HEAT',
                        'RESISTANCE', 'ABSORPTANCE', 'TRANSMITTANCE', 'EMISSIVITY',
                        'VISCOSITY', 'THERMAL-CAPACITY', 'VAPOUR-DIFFUSION-RESISTANCE-FACTOR',
                        'VAPOUR-DIFFUSIVITY-FACTOR', 'THICKNESS_MAX', 'THICKNESS_MIN',
                        'POROSITY', 'WATER-VAPOUR-DIFFUSION-RESISTANCE', 'REFERENCE-WATER-CONTENT',
                        'SHADING-COEF', 'GLASS-CONDUCTANCE', 'FRAME-WIDTH', 'FRAME-CONDUCT',
                        'FRAME-ABS', 'PORCENTAGE', 'INF-COEF', 'porcentajeIncrementoU',
                        'TransmisividadJulio', 'TRANSMITANCIA', 'SHADE-COEF-SUMMER',
                        'SHADE-COEF-WINTER', 'MARKER-SUMMER', 'MARKER-WINTER', 'TYPE-DEFINITION'
                    ]

                    if key in numeric_keys:
                        current_entity[key] = safe_float_convert(value)
                    else:
                        current_entity[key] = value

            # End of entity definition
            elif line == '..':
                if current_entity and entity_type:
                    save_entity(current_entity, entity_type, material_subtype,
                              materials_properties, materials_resistance, layers,
                              glass_types, frames, gaps)
                current_entity = None
                entity_type = None
                material_subtype = None

    output_file = f"{os.path.splitext(input_file)[0]}_results.xlsx"
    print(f"Parsing BDC file '{input_file}'")

    print(f"Found {len(materials_properties)} PROPERTIES materials")
    print(f"Found {len(materials_resistance)} RESISTANCE materials")
    print(f"Found {len(layers)} layers")
    print(f"Found {len(glass_types)} glass types")
    print(f"Found {len(frames)} frames")
    print(f"Found {len(gaps)} gaps")

    print("Writing to Excel file...")
    write_bdc_to_excel(materials_properties, materials_resistance, layers,
                       glass_types, frames, gaps, output_file)

    print(f"Successfully created {output_file}")

    return materials_properties, materials_resistance, layers, glass_types, frames, gaps

def save_entity(entity, entity_type, material_subtype, materials_properties,
                materials_resistance, layers, glass_types, frames, gaps):
    """Helper function to save entity to appropriate list"""
    if entity_type == 'MATERIAL' and material_subtype:
        if material_subtype == 'PROPERTIES':
            materials_properties.append(entity)
        elif material_subtype == 'RESISTANCE':
            materials_resistance.append(entity)
    elif entity_type == 'LAYERS':
        layers.append(entity)
    elif entity_type == 'GLASS-TYPE':
        glass_types.append(entity)
    elif entity_type == 'NAME-FRAME':
        frames.append(entity)
    elif entity_type == 'GAP':
        gaps.append(entity)

def write_bdc_to_excel(materials_properties, materials_resistance, layers,
                       glass_types, frames, gaps, output_filename):
    """
    Write BDC entities to Excel file with separate sheets
    """
    with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:

        # Write PROPERTIES materials
        if materials_properties:
            df = pd.DataFrame(materials_properties)
            cols = ['NAME'] + [col for col in df.columns if col != 'NAME']
            df = df[cols]
            df.to_excel(writer, sheet_name='Materials_Properties', index=False)

        # Write RESISTANCE materials
        if materials_resistance:
            df = pd.DataFrame(materials_resistance)
            cols = ['NAME'] + [col for col in df.columns if col != 'NAME']
            df = df[cols]
            df.to_excel(writer, sheet_name='Materials_Resistance', index=False)

        # Write layers
        if layers:
            df = pd.DataFrame(layers)
            cols = ['NAME'] + [col for col in df.columns if col != 'NAME']
            df = df[cols]
            df.to_excel(writer, sheet_name='Layers', index=False)

        # Write glass types
        if glass_types:
            df = pd.DataFrame(glass_types)
            cols = ['NAME'] + [col for col in df.columns if col != 'NAME']
            df = df[cols]
            df.to_excel(writer, sheet_name='Glass_Types', index=False)

        # Write frames
        if frames:
            df = pd.DataFrame(frames)
            cols = ['NAME'] + [col for col in df.columns if col != 'NAME']
            df = df[cols]
            df.to_excel(writer, sheet_name='Frames', index=False)

        # Write gaps (windows/doors)
        if gaps:
            df = pd.DataFrame(gaps)
            cols = ['NAME'] + [col for col in df.columns if col != 'NAME']
            df = df[cols]
            df.to_excel(writer, sheet_name='Gaps', index=False)

def process_bdc_library_file(input_file):
    """
    Parse the materials database file and separate PROPERTIES and RESISTANCE materials
    """
    properties_materials = []
    resistance_materials = []
    current_material = None
    material_type = None

    with open(input_file, 'r', encoding='iso-8859-1') as f:
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

    output_file = f"{os.path.splitext(input_file)[0]}_results.xlsx"
    print(f"Parsing materials file '{input_file}'")

    print(f"Found {len(properties_materials)} PROPERTIES materials")
    pprint(properties_materials)
    print(f"Found {len(resistance_materials)} RESISTANCE materials")
    pprint(resistance_materials)
    print("Writing to Excel file...")
    if properties_materials or resistance_materials:
        write_materials_to_excel(properties_materials, resistance_materials, output_file)

    print(f"Successfully created {output_file}")

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
	import argparse
	import glob

	"""Command line interface for BDC to Excel conversion."""
	parser = argparse.ArgumentParser(description="Convert BDC files to Excel format")
	parser.add_argument("-i", "--input", required=False,
	                    default=r'C:\ProgramasCTEyCEE\CTEHE2019\Libreria\BDCatalogo.bdc',
	                    help="Input file path (.bdc) or input directory path (processes all *.bdc files)")

	args = parser.parse_args()

	# Get absolute path of input
	input_path = os.path.abspath(args.input)

	# Check if input exists
	if not os.path.exists(input_path):
		print(f"Error: Input path does not exist: {input_path}")
		exit(1)

	# Determine if input is a file or directory
	if os.path.isfile(input_path):
		# Process single file
		file_ext = os.path.splitext(input_path)[1].lower()

		if file_ext == '.bdc':
			# Process .ctedbxml file
			process_bdc_file(input_path)
		else:
			print(f"Error: Unsupported file extension: {file_ext}")
			print("Supported extensions: .ctehexml, .ctedbxml")
			exit(1)

	elif os.path.isdir(input_path):
		# Process directory - find all .ctehexml files
		process_directory(input_path)

	else:
		print(f"Error: Input path is neither a file nor a directory: {input_path}")
		exit(1)
