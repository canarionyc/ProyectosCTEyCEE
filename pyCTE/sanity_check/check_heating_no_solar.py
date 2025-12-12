# %% setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4.builder import FAST

# ==========================================
# 1. SETUP & INPUTS
# ==========================================

# Building Physics Inputs
U_GLOBAL = 0.58  # W/m2K (Global heat transfer coefficient of envelope)
AREA_ENVELOPE = 8*4*4  # m2 (Surface area in contact with exterior)
FLOOR_AREA = 8*8.0  # m2 (Useful floor area for final KPI)
VOLUME_AIR = 8*8*3.5  # m3 (Internal air volume)
ACH = 0.6  # Air Changes per Hour (Ventilation + Infiltration)
T_SETPOINT_HEATING = 21.0  # °C (Thermostat setting)

# File Inputs
WEATHER_FILE_PATH = r'C:\ProyectosCTEyCEE\data\WeatherData\zonac_e1.epw'  # Replace with your local EPW file path
USE_DUMMY_DATA = False  # Set to False to load the real EPW file above


# ==========================================
# 2. HELPER FUNCTIONS
# ==========================================

def calculate_transmission_coeff(u_val, area):
    """Calculates H_tr (W/K)"""
    return u_val * area


def calculate_ventilation_coeff(volume, ach):
    """Calculates H_ve (W/K). 0.34 is volumetric heat cap of air in Wh/m3K"""
    return 0.34 * volume * ach


def load_epw_weather(filepath):
    """
    Parses a standard EPW file to get Dry Bulb Temperature.
    EPW format usually has data starting around row 8,
    and Dry Bulb Temp is typically column 6 (0-indexed).
    """
    # EPW files are CSV-like but have headers. We skip commonly 8 rows.
    # Column 6 is usually Dry Bulb Temperature.
    try:
        data = pd.read_csv(filepath, skiprows=8, header=None)
        # Verify length (8760 hours in a year)
        if len(data) < 8760:
            print("Warning: Weather file has fewer than 8760 rows.")

        # Extract Dry Bulb Temperature (Column 6)
        temps = data.iloc[0:8760, 6].values
        return temps
    except Exception as e:
        print(f"Error reading EPW: {e}")
        return None


def generate_dummy_weather():
    """Generates a synthetic yearly temperature curve for testing."""
    hours = np.arange(8760)
    # Model: Base 15C, Annual swing +/- 10C, Daily swing +/- 5C
    temp_annual = -10 * np.cos(2 * np.pi * hours / 8760)
    temp_daily = 5 * np.sin(2 * np.pi * hours / 24)
    return 15 + temp_annual + temp_daily


# ==========================================
# 3. CALCULATION ENGINE
# ==========================================

def run_simulation():
    # 1. Get Coefficients (W/K)
    H_tr = calculate_transmission_coeff(U_GLOBAL, AREA_ENVELOPE)
    H_ve = calculate_ventilation_coeff(VOLUME_AIR, ACH)
    H_total = H_tr + H_ve

    print(f"--- Physics Parameters ---")
    print(f"Transmission Coeff (H_tr): {H_tr:.2f} W/K")
    print(f"Ventilation Coeff (H_ve):  {H_ve:.2f} W/K")
    print(f"Total Heat Loss Coeff:     {H_total:.2f} W/K")
    print("-" * 30)

    # 2. Get Weather Data
    if USE_DUMMY_DATA:
        print("Using Synthetic Dummy Weather Data...")
        T_out_series = generate_dummy_weather()
    else:
        print(f"Loading weather from {WEATHER_FILE_PATH}...")
        T_out_series = load_epw_weather(WEATHER_FILE_PATH)
        if T_out_series is None:
            return

    # 3. Calculate Hourly Demand
    # Create DataFrame
    df = pd.DataFrame({'T_out': T_out_series})
    df['Hour'] = df.index + 1

    # Calculate Delta T (Heating is needed only when T_out < T_setpoint)
    # We use .clip(lower=0) to ensure we ignore cooling demand (negative values)
    df['Delta_T'] = (T_SETPOINT_HEATING - df['T_out']).clip(lower=0)

    # Calculate Power (W) -> Energy (Wh) per hour
    # Q = H_total * Delta_T
    df['Heating_Demand_Wh'] = H_total * df['Delta_T']

    # Convert to kWh
    df['Heating_Demand_kWh'] = df['Heating_Demand_Wh'] / 1000.0

    # 4. Aggregate Results
    total_annual_kwh = df['Heating_Demand_kWh'].sum()
    specific_demand = total_annual_kwh / FLOOR_AREA

    # ==========================================
    # 4. REPORTING
    # ==========================================
    print(f"\n--- Results ---")
    print(f"Total Annual Heating Demand: {total_annual_kwh:.2f} kWh")
    print(f"Specific Heating Demand:     {specific_demand:.2f} kWh/m2/year")

    # Optional: Basic Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(df['T_out'], label='Outside Temp', alpha=0.5, color='blue', linewidth=0.5)
    plt.axhline(y=T_SETPOINT_HEATING, color='r', linestyle='--', label='Setpoint')
    plt.title('Outside Temperature vs Setpoint')
    plt.xlabel('Hour of Year')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()

    # Breakdown of extreme days
    max_load_hour = df.loc[df['Heating_Demand_kWh'].idxmax()]
    print(f"\nPeak Load Event occurred at Hour {int(max_load_hour['Hour'])}")
    print(f"Outside Temp: {max_load_hour['T_out']:.2f}°C | Demand: {max_load_hour['Heating_Demand_kWh']:.2f} kW")


if __name__ == "__main__":
    run_simulation()
