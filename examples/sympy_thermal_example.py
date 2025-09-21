import sympy as sp
import pint

# Create pint unit registry for unit conversions
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# Define symbols for heat transfer equations
x, t = sp.symbols('x t')  # position and time
k, rho, cp = sp.symbols('k rho c_p')  # thermal conductivity, density, specific heat
T = sp.Function('T')(x, t)  # temperature as a function of position and time
q = sp.Function('q')(x, t)  # heat flux as a function of position and time

# Example 1: Heat equation in one dimension
# The heat equation: ∂T/∂t = α * ∂²T/∂x²
# where α = k/(ρ*cp) is thermal diffusivity
diffusivity = k / (rho * cp)
heat_eq = sp.Eq(sp.diff(T, t), diffusivity * sp.diff(T, x, x))

print("Heat Equation:")
print(sp.pretty(heat_eq))

# Example 2: Steady-state heat conduction through a wall (Fourier's Law)
# For steady state: ∂T/∂t = 0, so ∂²T/∂x² = 0
# The solution is T(x) = C1*x + C2
x_sym = sp.symbols('x')
T_steady = sp.Function('T')(x_sym)
steady_heat_eq = sp.Eq(sp.diff(T_steady, x_sym, x_sym), 0)
solution = sp.dsolve(steady_heat_eq, T_steady)

print("\nSteady State Heat Equation:")
print(sp.pretty(steady_heat_eq))
print("Solution:")
print(sp.pretty(solution))

# Example 3: Derive the thermal resistance formula R = e/λ
e, lambda_sym = sp.symbols('e lambda')
q_fourier = sp.symbols('q')  # heat flux
delta_T = sp.symbols('Delta_T')  # temperature difference

# Fourier's Law: q = -k * dT/dx
# For 1D steady-state through a uniform material: q = lambda * Delta_T / e
fourier_law = sp.Eq(q_fourier, lambda_sym * delta_T / e)
thermal_resistance = sp.symbols('R')
resistance_def = sp.Eq(thermal_resistance, e / lambda_sym)

# Substitute resistance into Fourier's law
heat_flow_with_R = sp.Eq(q_fourier, delta_T / thermal_resistance)

print("\nThermal Resistance Derivation:")
print("Fourier's Law:")
print(sp.pretty(fourier_law))
print("Thermal Resistance Definition:")
print(sp.pretty(resistance_def))
print("Heat flow in terms of resistance:")
print(sp.pretty(heat_flow_with_R))

# Example 4: Calculate U-value for multi-layer wall as in the document
R_si, R_se = sp.symbols('R_si R_se')  # surface resistances
R1, R2, R3 = sp.symbols('R_1 R_2 R_3')  # layer resistances
R_total = R_si + R1 + R2 + R3 + R_se
U_value = 1 / R_total

print("\nMulti-layer Wall U-value:")
print(f"R_total = {sp.pretty(R_total)}")
print(f"U-value = {sp.pretty(U_value)}")

# Substitute values (using same example as in pint)
values = {
    R_si: 0.13,
    R_se: 0.04,
    R1: 0.1 / 0.6,     # 10cm of brick with k=0.6 W/(m·K)
    R2: 0.05 / 0.035,  # 5cm of mineral wool with k=0.035 W/(m·K)
    R3: 0.01 / 0.14    # 1cm of wood with k=0.14 W/(m·K)
}

R_total_value = R_total.subs(values).evalf()
U_value_value = U_value.subs(values).evalf()

print(f"With values substituted:")
print(f"R_total = {R_total_value:.3f} m²·K/W")
print(f"U-value = {U_value_value:.3f} W/(m²·K)")