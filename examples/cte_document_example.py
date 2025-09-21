import pint
import numpy as np
import matplotlib.pyplot as plt

# Set up unit registry
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

def calculate_resistance_from_layers(layers, r_si, r_se):
    """
    Calculate total thermal resistance using equation (2) from the document:
    RT = Rsi + R1 + R2 + ... + Rn + Rse
    """
    return r_si + sum(thickness / conductivity for thickness, conductivity in layers) + r_se

def calculate_u_value(r_total):
    """
    Calculate U-value using equation (1) from the document:
    U = 1/RT
    """
    return 1 / r_total

def calc_temperature_profile(layers, t_inside, t_outside, r_si, r_se):
    """Calculate temperature at each layer interface"""
    r_total = calculate_resistance_from_layers(layers, r_si, r_se)
    u_value = calculate_u_value(r_total)
    
    # Heat flux (W/m²)
    q = u_value * (t_inside - t_outside)
    
    # Calculate temperatures at interfaces
    temps = [t_inside]
    r_cumulative = r_si
    temp_current = t_inside
    
    # Calculate drop across interior surface
    temp_drop = q * r_si
    temp_current -= temp_drop
    temps.append(temp_current)
    
    # Calculate drop across each material layer
    for thickness, conductivity in layers:
        r_layer = thickness / conductivity
        temp_drop = q * r_layer
        temp_current -= temp_drop
        temps.append(temp_current)
    
    return temps, q, r_total

# Example wall from the document
# Table 1 values for surface resistances
r_si_vert = Q_(0.13, 'm²*K/W')  # Vertical wall, interior
r_se_vert = Q_(0.04, 'm²*K/W')  # Vertical wall, exterior

# Example wall construction (from document examples)
wall_construction = [
    # [thickness (m), conductivity (W/m·K)]
    [Q_(0.115, 'm'), Q_(0.543, 'W/(m*K)')],    # Perforated brick
    [Q_(0.05, 'm'), Q_(0.034, 'W/(m*K)')],     # Thermal insulation
    [Q_(0.07, 'm'), Q_(0.301, 'W/(m*K)')],     # Air cavity + brick
]

# Calculate R-value, U-value and temperature profile
t_inside = Q_(20, 'degC')
t_outside = Q_(0, 'degC')
temps, heat_flux, r_total = calc_temperature_profile(
    wall_construction, t_inside, t_outside, r_si_vert, r_se_vert)
u_value = calculate_u_value(r_total)

# Print results
print(f"Wall construction calculation using method from DA DB-HE / 1:")
print(f"Total thermal resistance: {r_total:.3f}")
print(f"U-value: {u_value:.3f}")
print(f"Heat flux: {heat_flux:.2f}")

# Calculate temperatures at each interface (including surfaces)
print("\nTemperature profile through wall:")
layers = ["Indoor air", "Interior surface"] + [f"After layer {i+1}" for i in range(len(wall_construction))]
for i, temp in enumerate(temps):
    print(f"{layers[i]}: {temp:.2f}")

# Plot temperature profile
thicknesses = [0] + [0] + [layer[0].magnitude for layer in wall_construction]
positions = np.cumsum(thicknesses)
temp_values = [temp.magnitude for temp in temps]

plt.figure(figsize=(10, 6))
plt.plot(positions, temp_values, 'ro-', linewidth=2)
plt.xlabel('Distance from interior surface (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution Through Wall')
plt.grid(True)

# Add layer annotations
plt.axvline(x=positions[1], color='k', linestyle='--')
for i in range(2, len(positions)-1):
    plt.axvline(x=positions[i], color='k', linestyle=':')
plt.axvline(x=positions[-1], color='k', linestyle='--')

# Add layer labels
for i in range(1, len(positions)-1):
    midpoint = (positions[i] + positions[i+1]) / 2
    if i == 1:
        plt.text(midpoint, 10, f"Layer {i}", ha='center')
    else:
        plt.text(midpoint, 10, f"Layer {i-1}", ha='center')

plt.savefig('wall_temperature_profile.png')
plt.show()