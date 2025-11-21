
#%%
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ladybug.epw import EPW
import numpy as np
from pathlib import Path

# Set working directory
os.chdir(r'C:\dev\pyCTE')
print(f"Working directory: {os.getcwd()}")

#%% 1. Read all EPW files and consolidate location data
def read_all_epw_files():
    """Read all EPW files and extract location and weather data"""
    weather_data_path = Path('data/WeatherData')
    epw_files = list(weather_data_path.glob('zonac_*.epw'))
    
    locations_data = []
    weather_data = {}
    
    print(f"Found {len(epw_files)} EPW files")
    
    for epw_file in epw_files:
        try:
            print(f"Reading {epw_file.name}...")
            epw_data = EPW(str(epw_file))
            
            # Extract location data
            location = epw_data.location
            zone_name = epw_file.stem  # filename without extension
            
            location_dict = {
                'zone': zone_name,
                'city': location.city if hasattr(location, 'city') else zone_name,
                'country': location.country if hasattr(location, 'country') else 'Spain',
                'latitude': location.latitude,
                'longitude': location.longitude,
                'elevation': location.elevation,
                'time_zone': location.time_zone,
                'station_id': location.station_id if hasattr(location, 'station_id') else 'N/A'
            }
            locations_data.append(location_dict)
            
            # Extract temperature data
            dry_bulb_temp = epw_data.dry_bulb_temperature
            weather_data[zone_name] = {
                'temperature': [temp for temp in dry_bulb_temp.values],
                'datetimes': dry_bulb_temp.datetimes
            }
            
        except Exception as e:
            print(f"Error reading {epw_file.name}: {e}")
    
    return locations_data, weather_data

# Read all EPW files
locations_data, weather_data = read_all_epw_files()

#%% Save location data to CSV
locations_df = pd.DataFrame(locations_data)
locations_df = locations_df.sort_values('zone')
output_path = 'output/epw_locations.csv'
locations_df.to_csv(output_path, index=False)
print(f"Location data saved to {output_path}")
print("\nLocation data summary:")
print(locations_df.to_string(index=False))

#%% 2. Create temperature plots for climate zones
def categorize_zones(zone_name):
    """Categorize zones into groups for plotting"""
    if 'alfa' in zone_name:
        return 'Alpha'
    elif zone_name.startswith('zonac_a'):
        return 'Zone A'
    elif zone_name.startswith('zonac_b'):
        return 'Zone B'
    elif zone_name.startswith('zonac_c'):
        return 'Zone C'
    elif zone_name.startswith('zonac_d'):
        return 'Zone D'
    elif zone_name.startswith('zonac_e'):
        return 'Zone E'
    else:
        return 'Other'

def create_temperature_plots():
    """Create temperature plots for different climate zones"""
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(3, 2, figsize=(15, 18))
    fig.suptitle('Temperature Analysis by Spanish Climate Zones', fontsize=16, fontweight='bold')
    
    # Group zones
    zone_groups = {
        'Zone A': [],
        'Alpha': [],
        'Zone B': [],
        'Zone C': [],
        'Zone D': [],
        'Zone E': []
    }
    
    # Categorize and group data
    for zone_name, data in weather_data.items():
        category = categorize_zones(zone_name)
        if category in zone_groups:
            zone_groups[category].append((zone_name, data))
    
    # Plot each group
    axes_flat = axes.flatten()
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    for idx, (group_name, zones) in enumerate(zone_groups.items()):
        if idx >= len(axes_flat) or not zones:
            continue
            
        ax = axes_flat[idx]
        
        # Calculate monthly averages for each zone in the group
        for zone_name, data in zones:
            temps = data['temperature']
            datetimes = data['datetimes']
            
            # Convert to pandas for easier manipulation
            df_temp = pd.DataFrame({
                'datetime': datetimes,
                'temperature': temps
            })
            df_temp['month'] = pd.to_datetime(df_temp['datetime']).dt.month
            monthly_avg = df_temp.groupby('month')['temperature'].mean()
            
            ax.plot(monthly_avg.index, monthly_avg.values, 
                   marker='o', linewidth=2, label=zone_name.replace('zonac_', '').upper())
        
        ax.set_title(f'{group_name} Climate Zones', fontweight='bold')
        ax.set_xlabel('Month')
        ax.set_ylabel('Temperature (°C)')
        ax.grid(True, alpha=0.3)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    
    # Remove empty subplots
    for idx in range(len(zone_groups), len(axes_flat)):
        fig.delaxes(axes_flat[idx])
    
    plt.tight_layout()
    plt.savefig('output/climate_zones_temperature_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

# Create temperature plots
create_temperature_plots()

#%% Create summary statistics
def create_temperature_statistics():
    """Create temperature statistics for all zones"""
    
    stats_data = []
    
    for zone_name, data in weather_data.items():
        temps = data['temperature']
        
        stats = {
            'zone': zone_name,
            'category': categorize_zones(zone_name),
            'min_temp': np.min(temps),
            'max_temp': np.max(temps),
            'mean_temp': np.mean(temps),
            'std_temp': np.std(temps),
            'temp_range': np.max(temps) - np.min(temps)
        }
        stats_data.append(stats)
    
    stats_df = pd.DataFrame(stats_data)
    stats_df = stats_df.sort_values(['category', 'zone'])
    
    # Save statistics
    stats_output_path = 'output/epw_temperature_statistics.csv'
    stats_df.to_csv(stats_output_path, index=False)
    print(f"\nTemperature statistics saved to {stats_output_path}")
    
    # Display statistics
    print("\nTemperature Statistics by Zone:")
    print(stats_df.round(2).to_string(index=False))
    
    return stats_df

# Create statistics
stats_df = create_temperature_statistics()

#%% Create a heatmap of monthly temperatures
def create_monthly_heatmap():
    """Create a heatmap showing monthly temperatures for all zones"""
    
    monthly_data = {}
    
    for zone_name, data in weather_data.items():
        temps = data['temperature']
        datetimes = data['datetimes']
        
        # Convert to pandas for easier manipulation
        df_temp = pd.DataFrame({
            'datetime': datetimes,
            'temperature': temps
        })
        df_temp['month'] = pd.to_datetime(df_temp['datetime']).dt.month
        monthly_avg = df_temp.groupby('month')['temperature'].mean()
        monthly_data[zone_name.replace('zonac_', '').upper()] = monthly_avg
    
    # Create DataFrame for heatmap
    heatmap_df = pd.DataFrame(monthly_data).T
    heatmap_df.columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Create heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_df, annot=True, cmap='RdYlBu_r', fmt='.1f', 
                cbar_kws={'label': 'Temperature (°C)'})
    plt.title('Monthly Average Temperatures by Climate Zone', fontsize=14, fontweight='bold')
    plt.ylabel('Climate Zone')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.savefig('output/monthly_temperature_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return heatmap_df

# Create heatmap
heatmap_df = create_monthly_heatmap()

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print("Files created:")
print("- output/epw_locations.csv - Location data for all zones")
print("- output/epw_temperature_statistics.csv - Temperature statistics")
print("- output/climate_zones_temperature_analysis.png - Temperature plots by zone")
print("- output/monthly_temperature_heatmap.png - Monthly temperature heatmap")
