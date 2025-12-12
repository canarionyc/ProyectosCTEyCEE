# %% setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. SETUP & INPUTS
# ==========================================

# --- Location (Required for Solar Geometry) ---
# Example: Madrid (Change to your building's location)
LATITUDE = 40.4168  # Degrees North
LONGITUDE = -3.7038  # Degrees East
TZ_MERIDIAN = 0  # EPW files often use Solar Time or UTC.
# For a sanity check, simplified solar time is sufficient.

# --- Building Physics ---
U_GLOBAL = 0.5  # W/m2K (Average U-value of opaque + glazed)
AREA_ENVELOPE = 200.0  # m2 (Total thermal envelope area)
FLOOR_AREA = 100.0  # m2
VOLUME_AIR = 250.0  # m3
ACH = 0.6  # Air Changes per Hour
T_SETPOINT_HEATING = 21.0  # °C

# --- Glazing Parameters (Constant Globals) ---
G_VALUE = 0.65  # Solar Heat Gain Coefficient (g-value)
FRAME_FACTOR = 0.25  # % of window area that is frame (no solar gain)

# Window Areas by Orientation (m2)
WIN_AREAS = {
    'S': 8.0,  # South
    'E': 4.0,  # East
    'N': 2.0,  # North
    'W': 4.0  # West
}

# --- Simulation Settings ---
# Set to False to load your real EPW file
USE_DUMMY_DATA = False
WEATHER_FILE_PATH = r'C:\ProyectosCTEyCEE\data\WeatherData\zonac_e1.epw'  # Replace with your local EPW file path


# ==========================================
# 2. SOLAR GEOMETRY ENGINE
# ==========================================

def calculate_solar_position(day_of_year, hour, lat_deg):
    """
    Calculates Solar Altitude and Azimuth for a specific hour/day/lat.
    """
    lat_rad = np.radians(lat_deg)

    # 1. Declination (delta) - Cooper's approximate equation
    declination = np.radians(23.45) * np.sin(2 * np.pi * (284 + day_of_year) / 365.0)

    # 2. Hour Angle (omega)
    # Solar noon = 12.0. Earth rotates 15 deg/hour.
    time_offset = (hour - 12.0)
    hour_angle = np.radians(15.0 * time_offset)

    # 3. Solar Altitude (alpha)
    sin_elev = (np.sin(lat_rad) * np.sin(declination) +
                np.cos(lat_rad) * np.cos(declination) * np.cos(hour_angle))
    sin_elev = np.clip(sin_elev, -1, 1)  # Safety clip
    altitude = np.arcsin(sin_elev)

    # 4. Solar Azimuth (phi)
    # Formula relates Azimuth to Altitude, Lat, and Declination
    cos_az = (np.sin(altitude) * np.sin(lat_rad) - np.sin(declination)) / \
             (np.cos(altitude) * np.cos(lat_rad) + 1e-6)
    cos_az = np.clip(cos_az, -1, 1)
    azimuth = np.arccos(cos_az)

    # Correct Azimuth quadrant (if morning, sun is East, azimuth negative)
    # Standard: South=0, East=-90 (negative), West=+90 (positive)
    if hour_angle < 0:
        azimuth = -azimuth

    return altitude, azimuth


def calculate_incident_gain(row, win_areas, g_val, frame_f):
    """
    Calculates Watts of solar gain entering the building for one timestep.
    """
    # If sun is below horizon, no gain
    if row['Altitude'] <= 0:
        return 0.0

    # Wall orientations (radians relative to South)
    wall_azimuths = {'S': 0, 'E': -np.pi / 2, 'W': np.pi / 2, 'N': np.pi}

    total_gain_W = 0.0

    for orient, area in win_areas.items():
        if area <= 0: continue

        # Incidence Angle (theta) on vertical surface
        # cos(theta) = cos(alpha) * cos(sun_azimuth - wall_azimuth)
        sun_wall_diff = row['Azimuth'] - wall_azimuths[orient]
        cos_theta = np.cos(row['Altitude']) * np.cos(sun_wall_diff)

        # 1. Direct Beam Component
        # Only added if sun is actually in front of the wall (cos_theta > 0)
        direct_flux = 0.0
        if cos_theta > 0:
            direct_flux = row['Direct_Normal_W'] * cos_theta

        # 2. Diffuse Component (Isotropic approx)
        # Vertical wall view factor is 0.5
        diffuse_flux = 0.5 * row['Diffuse_Horiz_W']

        # Total Gain
        # Q_sol = (I_dir + I_diff) * Area * g * (1 - frame)
        gain = (direct_flux + diffuse_flux) * area * g_val * (1 - frame_f)
        total_gain_W += gain

    return total_gain_W


# ==========================================
# 3. DATA LOADING & GENERATION
# ==========================================

def load_epw_weather(filepath):
    try:
        # Standard EPW columns (0-indexed):
        # 6: Dry Bulb Temp, 14: Direct Normal Rad, 15: Diffuse Horizontal Rad
        data = pd.read_csv(filepath, skiprows=8, header=None)
        df = pd.DataFrame()
        df['T_out'] = data.iloc[0:8760, 6]
        df['Direct_Normal_W'] = data.iloc[0:8760, 14]
        df['Diffuse_Horiz_W'] = data.iloc[0:8760, 15]

        # Time columns
        df['Hour_Year'] = np.arange(8760)
        df['Day_Year'] = (df['Hour_Year'] // 24) + 1
        df['Hour_Day'] = (df['Hour_Year'] % 24) + 1
        return df
    except Exception as e:
        print(f"Error reading EPW: {e}. Check file path/format.")
        return None


def generate_dummy_data():
    """Generates synthetic Temp and Solar data for testing"""
    hours = np.arange(8760)
    day_year = (hours // 24) + 1
    hour_day = (hours % 24)

    # Temp
    t_out = 12 - 10 * np.cos(2 * np.pi * hours / 8760) + 5 * np.sin(2 * np.pi * hours / 24 - np.pi)

    # Solar (Simple model: Sun up 6am-6pm)
    seasonal = 1.0 - 0.3 * np.cos(2 * np.pi * day_year / 365)
    dni = np.maximum(0, 800 * np.sin(np.pi * (hour_day - 6) / 12)) * seasonal
    dhi = np.maximum(0, 100 * np.sin(np.pi * (hour_day - 6) / 12)) * seasonal

    return pd.DataFrame({
        'T_out': t_out, 'Direct_Normal_W': dni, 'Diffuse_Horiz_W': dhi,
        'Hour_Year': hours, 'Day_Year': day_year, 'Hour_Day': hour_day
    })


# ==========================================
# 4. MAIN CALCULATION
# ==========================================

def run_simulation():
    # 1. Load Weather
    if USE_DUMMY_DATA:
        print("Using Synthetic Dummy Data...")
        df = generate_dummy_data()
    else:
        print(f"Loading {WEATHER_FILE_PATH}...")
        df = load_epw_weather(WEATHER_FILE_PATH)
        if df is None: return

    # 2. Physics Coefficients
    H_tr = U_GLOBAL * AREA_ENVELOPE
    H_ve = 0.34 * VOLUME_AIR * ACH
    H_total = H_tr + H_ve
    print(f"Total Heat Transfer Coefficient (H_tr + H_ve): {H_total:.2f} W/K")

    # 3. Solar Calculations
    print("Calculating Solar Geometry...")
    # Vectorized solar position calculation for speed
    vec_pos = np.vectorize(calculate_solar_position)
    df['Altitude'], df['Azimuth'] = vec_pos(df['Day_Year'], df['Hour_Day'], LATITUDE)

    print("Calculating Solar Gains...")
    # Row-by-row gain calculation
    df['Solar_Gain_W'] = df.apply(
        lambda row: calculate_incident_gain(row, WIN_AREAS, G_VALUE, FRAME_FACTOR),
        axis=1
    )

    # 4. Energy Balance
    # Raw Heating Need (Losses only)
    df['Heat_Loss_W'] = H_total * (T_SETPOINT_HEATING - df['T_out'])

    # Net Heating Need (Losses - Solar Gains), floor at 0
    df['Net_Heating_Power_W'] = (df['Heat_Loss_W'] - df['Solar_Gain_W']).clip(lower=0)

    # 5. Results
    total_demand_kWh = df['Net_Heating_Power_W'].sum() / 1000.0
    specific_demand = total_demand_kWh / FLOOR_AREA

    print("-" * 30)
    print(f"RESULTS FOR LOCATION: {LATITUDE}N, {LONGITUDE}E")
    print(f"Annual Net Heating Demand: {total_demand_kWh:.2f} kWh")
    print(f"Specific Demand:           {specific_demand:.2f} kWh/m2/year")

    # Savings check
    gross_demand = df['Heat_Loss_W'].clip(lower=0).sum() / 1000.0
    print(f"Gross Demand (No Solar):   {gross_demand:.2f} kWh")
    print(f"Solar Savings:             {gross_demand - total_demand_kWh:.2f} kWh")
    print("-" * 30)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(df['Hour_Year'], df['Heat_Loss_W'].clip(lower=0) / 1000, label='Gross Loss (kW)', alpha=0.3)
    plt.plot(df['Hour_Year'], df['Net_Heating_Power_W'] / 1000, label='Net Heating Need (kW)', color='red',
             linewidth=0.5)
    plt.title('Heating Demand: Gross vs Net (Solar Corrected)')
    plt.xlabel('Hour of Year')
    plt.ylabel('Power (kW)')
    plt.legend()
    plt.savefig('heating_demand_solar.png')  # Saving instead of showing
    print("Plot saved as heating_demand_solar.png")

if __name__ == "__main__":
    run_simulation()