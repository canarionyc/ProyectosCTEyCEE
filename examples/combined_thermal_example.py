import sympy as sp
import pint
import numpy as np
import matplotlib.pyplot as plt

# Set up pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# Function to calculate thermal resistance for a wall component using the formulas from the document
def calculate_wall_resistance(layers, r_si=0.13, r_se=0.04):
    """
    Calculate total thermal resistance of a wall
    
    Parameters:
    - layers: list of [thickness (m), conductivity (W/m·K)] pairs
    - r_si: interior surface resistance (m²·K/W)
    - r_se: exterior surface resistance (m²·K/W)
    
    Returns:
    - R-value in m²·K/W
    """
    r_total = r_si + sum(e/k for e, k in layers) + r_se
    return r_total

# Define a symbolic function to derive temperature profile equation
def derive_temp_profile():
    """Derive equation for temperature profile through a wall"""
    # Define symbols
    x = sp.symbols('x')  # position through wall
    L = sp.symbols('L')  # wall thickness
    T_i = sp.symbols('T_i')  # indoor temperature
    T_o = sp.symbols('T_o')  # outdoor temperature
    k = sp.symbols('k')     # thermal conductivity
    
    # For steady state conditions, the temperature profile is linear
    # T(x) = T_i + (T_o - T_i) * x/L
    T = sp.Function('T')
    profile_eq = sp.Eq(T(x), T_i + (T_o - T_i) * x/L)
    
    # Heat flux equation using Fourier's law
    q_eq = sp.Eq(sp.symbols('q'), -k * sp.diff(T(x), x))
    q_substituted = q_eq.subs(T(x), profile_eq.rhs)
    
    return profile_eq, q_substituted

# Practical building physics example: Energy loss calculation for a house
def building_energy_loss(walls, windows, temps_monthly, building_dims):
    """
    Calculate monthly energy loss through building envelope
    
    Parameters:
    - walls: Dictionary of wall constructions with areas and R-values
    - windows: Dictionary of window constructions with areas and U-values
    - temps_monthly: Monthly average temperatures (outside)
    - building_dims: Building dimensions
    
    Returns:
    - Monthly energy losses in kWh
    """
    # Interior temperature
    t_interior = Q_(21, 'degC')
    
    # Calculate energy loss for each month
    energy_loss_monthly = []
    
    for month, t_exterior in enumerate(temps_monthly):
        # Hours in month (approximately)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        hours = days_in_month[month] * 24
        
        # Calculate loss through each wall
        wall_loss = sum(
            area * (1 / r_value) * (t_interior - t_exterior) * hours
            for name, (area, r_value) in walls.items()
        )
        
        # Calculate loss through windows
        window_loss = sum(
            area * u_value * (t_interior - t_exterior) * hours
            for name, (area, u_value) in windows.items()
        )
        
        # Total loss
        total_loss = wall_loss + window_loss
        energy_loss_monthly.append(total_loss.to('kWh'))
    
    return energy_loss_monthly

# Example usage
if __name__ == "__main__":
    # Print the derived temperature profile equation
    temp_eq, heat_flux_eq = derive_temp_profile()
    print("Temperature profile equation:")
    print(sp.pretty(temp_eq))
    print("\nHeat flux equation:")
    print(sp.pretty(heat_flux_eq))
    
    # Define wall constructions (similar to examples from the document)
    # Format: [thickness (m), conductivity (W/m·K)]
    exterior_wall = [
        [Q_(0.102, 'm'), Q_(0.89, 'W/(m*K)')],    # Brick
        [Q_(0.05, 'm'), Q_(0.035, 'W/(m*K)')],    # Mineral wool insulation
        [Q_(0.013, 'm'), Q_(0.25, 'W/(m*K)')],    # Gypsum board
    ]
    
    roof = [
        [Q_(0.025, 'm'), Q_(0.13, 'W/(m*K)')],    # Wood 
        [Q_(0.1, 'm'), Q_(0.04, 'W/(m*K)')],      # Fiberglass insulation
        [Q_(0.013, 'm'), Q_(0.25, 'W/(m*K)')],    # Gypsum board
    ]
    
    # Calculate R-values
    r_ext_wall = calculate_wall_resistance(exterior_wall)
    r_roof = calculate_wall_resistance(roof, r_si=0.10, r_se=0.04)  # Different r_si for roof
    
    print(f"\nExterior wall R-value: {r_ext_wall:.3f} m²·K/W")
    print(f"Exterior wall U-value: {(1/r_ext_wall):.3f} W/(m²·K)")
    print(f"Roof R-value: {r_roof:.3f} m²·K/W")
    print(f"Roof U-value: {(1/r_roof):.3f} W/(m²·K)")
    
    # Convert to imperial (R-value in ft²·°F·h/BTU)
    r_ext_wall_imperial = r_ext_wall * Q_(5.678, '(ft²·°F·h/BTU)/(m²·K/W)')
    r_roof_imperial = r_roof * Q_(5.678, '(ft²·°F·h/BTU)/(m²·K/W)')
    
    print(f"\nExterior wall R-value: {r_ext_wall_imperial:.1f}")
    print(f"Roof R-value: {r_roof_imperial:.1f}")
    
    # Building dimensions
    building_dims = {
        "length": Q_(10, 'm'),
        "width": Q_(8, 'm'),
        "height": Q_(2.7, 'm')
    }
    
    # Calculate areas
    wall_area = 2 * (building_dims["length"] + building_dims["width"]) * building_dims["height"]
    window_area = Q_(15, 'm²')  # Assume 15 m² of windows
    net_wall_area = wall_area - window_area
    roof_area = building_dims["length"] * building_dims["width"]
    
    # Define envelope components
    walls = {
        "exterior_walls": (net_wall_area, r_ext_wall)
    }
    
    windows = {
        "double_glazed": (window_area, Q_(2.8, 'W/(m²*K)'))
    }
    
    # Monthly average temperatures for a sample location (°C)
    temps_monthly = [
        Q_(2, 'degC'), Q_(3, 'degC'), Q_(6, 'degC'), Q_(9, 'degC'), 
        Q_(14, 'degC'), Q_(17, 'degC'), Q_(20, 'degC'), Q_(19, 'degC'),
        Q_(16, 'degC'), Q_(11, 'degC'), Q_(6, 'degC'), Q_(3, 'degC')
    ]
    
    # Calculate monthly energy loss
    energy_loss = building_energy_loss(
        walls={"exterior_walls": (net_wall_area, r_ext_wall), 
               "roof": (roof_area, r_roof)},
        windows=windows,
        temps_monthly=temps_monthly,
        building_dims=building_dims
    )
    
    # Display results
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    print("\nMonthly energy loss:")
    for i, month in enumerate(months):
        print(f"{month}: {energy_loss[i]:.1f}")
    
    # Calculate annual energy loss
    annual_loss = sum(energy_loss)
    print(f"\nTotal annual energy loss: {annual_loss:.1f}")
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.bar(months, [e.magnitude for e in energy_loss])
    plt.title('Monthly Building Heat Loss')
    plt.xlabel('Month')
    plt.ylabel('Energy Loss (kWh)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('monthly_heat_loss.png')
    plt.show()