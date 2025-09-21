#%%
import pint
import numpy as np
import matplotlib.pyplot as plt

from pycte import ureg, Quantity as Q_

#%% Example 1: Basic thermal resistance calculation of a wall (from the document)
def calc_thermal_resistance(thickness, conductivity):
    """Calculate thermal resistance R = e/λ as in equation (3) of the document"""
    return thickness / conductivity

# Materials with their thermal conductivity in W/(m·K)
materials = {
    'Concrete': Q_(1.5, 'W/(m*K)'),
    'Brick': Q_(0.6, 'W/(m*K)'),
    'Mineral wool': Q_(0.035, 'W/(m*K)'),
    'Wood': Q_(0.14, 'W/(m*K)')
}

# Calculate resistance for a 10cm thick layer of each material
for material, conductivity in materials.items():
    thickness = Q_(0.1, 'm')
    resistance = calc_thermal_resistance(thickness, conductivity)
    print(f"{material} layer of {thickness:~} has R-value: {resistance:~.3f} or {resistance.to('ft²·°F·h/BTU'):~.3f}")

#%% Example 2: Total thermal resistance of a multi-layer wall
# Following the document equation (2): RT = Rsi + R1 + R2 + ... + Rn + Rse
def calc_total_resistance(layers, r_si, r_se):
    """Calculate total thermal resistance including surface resistances"""
    return r_si + sum(thickness / conductivity for thickness, conductivity in layers) + r_se

# Define a wall with [thickness, conductivity] pairs
wall_layers = [
    [Q_(0.1, 'm'), materials['Brick']],
    [Q_(0.05, 'm'), materials['Mineral wool']],
    [Q_(0.01, 'm'), materials['Wood']]
]

# Surface resistances from Table 1 in the document
r_si = Q_(0.13, 'm²*K/W')  # interior
r_se = Q_(0.04, 'm²*K/W')  # exterior

r_total = calc_total_resistance(wall_layers, r_si, r_se)
u_value = 1 / r_total

print(f"\nMulti-layer wall total resistance: {r_total:~.3f}")
print(f"U-value: {u_value:~.3f}")

#%% Example 3: Temperature gradient through wall
def temperature_profile(wall_layers, t_inside, t_outside, r_si, r_se):
    """Calculate temperatures at each layer interface"""
    r_total = calc_total_resistance(wall_layers, r_si, r_se)
    q = (t_inside - t_outside) / r_total  # heat flux
    
    # Start from inside temperature
    temps = [t_inside]
    r_cumulative = r_si
    
    # Calculate temperature at each interface
    for thickness, conductivity in wall_layers:
        r_layer = thickness / conductivity
        temp_drop = q * r_layer
        temps.append(temps[-1] - temp_drop)
        r_cumulative += r_layer
    
    return temps, q

# Calculate temperature through the wall with 20°C inside and 0°C outside
t_inside = Q_(20, 'degC')
t_outside = Q_(0, 'degC')
temps, q = temperature_profile(wall_layers, t_inside, t_outside, r_si, r_se)

# Convert temperatures to a list of values for plotting
temps_values = [temp.magnitude for temp in temps]
layer_names = ['Inside'] + [f'After {i+1}' for i in range(len(wall_layers))]

print(f"\nHeat flux: {q:~.2f}")
print("Temperature profile through wall:")
for i, temp in enumerate(temps):
    print(f"{layer_names[i]}: {temp:~.1f}")

# Convert imperial to SI units
insulation_imperial = Q_(0.02, 'BTU*in/(h*ft²*°F)')
insulation_si = insulation_imperial.to('W/(m*K)')
print(f"\nConverting units: {insulation_imperial:~} = {insulation_si:~.4f}")