# %% setup
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import glob
from pathlib import Path

#%%

def parse_met_file(file_path):
    """
    Parse a single .MET file and return a DataFrame with the data.

    Args:
        file_path (str): Path to the .MET file

    Returns:
        pandas.DataFrame: DataFrame containing the meteorological data
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Extract file identifier from first line
    file_identifier = lines[0].strip()

    # Extract location data from second line
    location_data = lines[1].strip().split()
    latitude = float(location_data[0])
    longitude = float(location_data[1])
    altitude = float(location_data[2])
    reference_longitude = float(location_data[3])

    # Extract zone name from filename
    zone_name = Path(file_path).stem

    # Parse hourly data (lines 2-8761, 0-indexed)
    hourly_data = []
    for i in range(2, min(len(lines), 8762)):  # Ensure we don't go beyond file length
        line = lines[i].strip()
        if line:  # Skip empty lines
            data_fields = line.split()
            if len(data_fields) >= 13:  # Ensure we have all required fields
                hourly_data.append([
                    zone_name,
                    file_identifier,
                    latitude,
                    longitude,
                    altitude,
                    reference_longitude,
                    int(data_fields[0]),      # Mes
                    int(data_fields[1]),      # Día
                    int(data_fields[2]),      # Hora
                    float(data_fields[3]),    # Temperatura seca
                    float(data_fields[4]),    # Temperatura efectiva del cielo
                    float(data_fields[5]),    # Irradiancia solar directa
                    float(data_fields[6]),    # Irradiancia solar difusa
                    float(data_fields[7]),    # Humedad específica
                    float(data_fields[8]),    # Humedad relativa
                    float(data_fields[9]),    # Velocidad del viento
                    float(data_fields[10]),   # Dirección del viento
                    float(data_fields[11]),   # Azimut solar
                    float(data_fields[12])    # Cénit solar
                ])

    # Create DataFrame
    columns = [
        'zona',
        'identificador_archivo',
        'latitud',
        'longitud',
        'altitud',
        'longitud_referencia',
        'mes',
        'dia',
        'hora',
        'temperatura_seca_C',
        'temperatura_efectiva_cielo_C',
        'irradiancia_solar_directa_W_m2',
        'irradiancia_solar_difusa_W_m2',
        'humedad_especifica_kg_kg',
        'humedad_relativa_pct',
        'velocidad_viento_m_s',
        'direccion_viento_grados',
        'azimut_solar_grados',
        'cenit_solar_grados'
    ]

    df = pd.DataFrame(hourly_data, columns=columns)
    return df

def combine_met_files_to_csv(input_directory, output_file):
    """
    Combine all .MET files in a directory into a single CSV file.

    Args:
        input_directory (str): Directory containing .MET files
        output_file (str): Output CSV file path
    """
    # Find all .MET files in the directory
    met_files = glob.glob(os.path.join(input_directory, "*.met"))

    if not met_files:
        print(f"No .MET files found in {input_directory}")
        return

    print(f"Found {len(met_files)} .MET files")

    all_dataframes = []

    # Process each .MET file
    for met_file in met_files:
        print(f"Processing: {os.path.basename(met_file)}")
        try:
            df = parse_met_file(met_file)
            all_dataframes.append(df)
            print(f"  - Successfully processed {len(df)} records")
        except Exception as e:
            print(f"  - Error processing {met_file}: {str(e)}")

    # Combine all DataFrames
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)

        # Save to CSV
        combined_df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"\nCombined data saved to: {output_file}")
        print(f"Total records: {len(combined_df)}")
        print(f"Zones processed: {combined_df['zona'].nunique()}")
        print(f"Unique zones: {sorted(combined_df['zona'].unique())}")

        # Display basic statistics
        print("\nBasic statistics:")
        print(f"Temperature range: {combined_df['temperatura_seca_C'].min():.1f}°C to {combined_df['temperatura_seca_C'].max():.1f}°C")
        print(f"Date range: Month {combined_df['mes'].min()} to {combined_df['mes'].max()}")

    else:
        print("No data to combine - all files failed to process")

if __name__ == "__main__":
    # Set the input directory and output file
    os.chdir("C:/dev/pyCTE"); print(os.getcwd())
    input_directory = "data/CTEdatosMET_20140418"
    output_file = "combined_meteorological_data.csv"

    # Combine all .MET files into a single CSV
    combine_met_files_to_csv(input_directory, output_file)

    print("\nScript completed!")