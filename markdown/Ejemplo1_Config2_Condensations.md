Of course. Here is a comprehensive extraction of all information related to **condensations** (`condensaciones`) from the document, focusing on the methodology for checking and preventing both interstitial and surface condensation.

The primary concern within the CTE DB-HE is the **limitation of interstitial condensation** within the building envelope, as it can degrade materials and reduce thermal performance.

### 1. Regulatory Requirement (HE1)

The document states the general requirement from Section HE 1 (Page 41):

> "In the case that interstitial condensations occur in the thermal envelope of the building, these shall be such that they do not produce a significant reduction in its thermal performance or pose a risk of degradation or loss of its service life. In no case shall the maximum accumulated condensation in each annual period exceed the amount of possible evaporation in the same period."

The verification is performed according to the supporting document **DA DB-HE/2**.

---

### 2. Types of Condensation Analysis

The document specifies two types, with a clear focus on the first:

1.  **Interstitial Condensation (`Condensaciones intersticiales`):** Condensation that occurs *inside* the layers of a construction assembly (e.g., inside the insulation or within the brickwork). **This is the primary analysis required.**
2.  **Surface Condensation (`Condensaciones superficiales`):** Condensation that forms on the visible interior surfaces of walls or windows. This is considered less critical for this project.

---

### 3. Methodology for Interstitial Condensation Analysis

The document provides a full, detailed example of the calculation for the **External Wall** (`Muro Exterior`), following the Glaser method (a steady-state vapor diffusion analysis).

#### Step 1: Data Preparation - Wall Characterization

The first step is to define the thermal and hygrothermal properties of each layer in the wall assembly.

**Data from Page 81 & 147:**

| CAPAS DEL CERRAMIENTO (Wall Layers) | espesor, e (m) | Cond. λ (W/m·K) | R (m²·K/W) | μ (-) | Sd (m) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Resistencia superficial exterior | - | - | 0.04 | - | - |
| 1 Mortero de cemento | 0.030 | 0.550 | 0.05 | 10 | 0.3 |
| 2 EPS Poliestireno | 0.140 | 0.038 | 3.68 | 20 | 2.8 |
| 3 1 pie Ladrillo Perforado | 0.240 | 0.667 | 0.36 | 10 | 2.4 |
| 4 Mortero de cemento | 0.010 | 0.550 | 0.02 | 10 | 0.1 |
| 5 Cámara de aire sin ventilar | 0.050 | - | 0.18 | 1 | 0.05 |
| 6 Placa de yeso laminado (PYL) | 0.015 | 0.250 | 0.06 | 4 | 0.06 |
| 7 Placa de yeso laminado (PYL) | 0.015 | 0.250 | 0.06 | 4 | 0.06 |
| Resistencia superficial interior | - | - | 0.13 | - | - |
| **TOTALES** | **0.500** | | **4.59** | | **5.77** |

**Key Parameters:**
*   **`μ` (Mu):** Vapor diffusion resistance factor. The higher the value, the more resistant the material is to vapor flow (a vapor barrier has a very high μ).
*   **`Sd`:** Equivalent air layer thickness. It is calculated as `Sd = e × μ`. This is the key property for the vapor diffusion calculation.

#### Step 2: Definition of Boundary Conditions

The analysis is performed for the most unfavorable average monthly conditions, which is **January**.

**Calculation of Exterior Conditions (for location: Albarracín) from Pages 82-83 & 148-149:**

1.  **Temperature:** The outside temperature is taken from the provincial capital (Teruel) and adjusted for altitude.
    *   Teruel (915m): `3.8 °C`
    *   Albarracín (1200m): `1.0 °C` (adjusted down by ~1°C per 100m altitude difference).

2.  **Vapor Pressure (`P_e`):** This is more complex, as relative humidity changes with temperature.
    a.  Calculate Saturation Pressure (`P_sat`) for Teruel at 3.8°C using the **Magnus formula**:
        `P_sat = 610.5 * exp( (17.269 * θ_e) / (237.3 + θ_e) )`
        `P_sat = 610.5 * exp( (17.269 * 3.8) / (237.3 + 3.8) ) = 801.48 Pa`
    b.  Calculate Actual Vapor Pressure (`P_e`) for Teruel:
        `P_e = HR_e * P_sat = 0.72 * 801.48 Pa = 577.06 Pa`
    c.  **Crucial Assumption:** The absolute humidity (vapor pressure) is the same in Albarracín. Calculate Saturation Pressure for Albarracín at 1.0°C:
        `P_sat.loc = 610.5 * exp( (17.269 * 1.0) / (237.3 + 1.0) ) = 656.38 Pa`
    d.  Calculate Relative Humidity for Albarracín:
        `HR_e.loc = P_e / P_sat.loc = 577.06 / 656.38 = 0.879 (88%)`

**Interior Conditions (Page 84 & 150):**
*   **Temperature (`θ_i`):** `20 °C`
*   **Relative Humidity (`HR_i`):** `55%` (for a residential building with normal humidity production).
*   **Interior Vapor Pressure (`P_i`):**
    `P_i = HR_i * P_sat(20°C) = 0.55 * 2337 Pa = 1285.35 Pa`
    *(Note: 2337 Pa is the saturation pressure at 20°C).*

#### Step 3: Temperature Distribution Calculation

The temperature at each interface between layers is calculated proportionally to the thermal resistance.

**Formula (Page 85 & 152):**
`θ_x = θ_e + ( (R_se + ΣR) / R_T ) * (θ_i - θ_e)`

**Where:**
*   `θ_x` = Temperature at a specific point [°C]
*   `ΣR` = Sum of resistances from the exterior up to that point [m²·K/W]
*   `R_T` = Total thermal resistance of the wall (4.59 m²·K/W)

**Resulting Temperature Distribution (from Page 87 & 153):**
| Point | Exterior | Surf. Ext. | Capa 1 | Capa 2 | Capa 3 | Capa 4 | Capa 5 | Capa 6 | Capa 7 | Surf. Int. | Interior |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Temp. (°C)** | 1.00 | 1.12 | 1.34 | 16.63 | 18.13 | 18.20 | 18.95 | 19.20 | 19.45 | 19.99 | 20.00 |

#### Step 4: Vapor Pressure Distribution Calculation

The vapor pressure at each interface is calculated proportionally to the vapor resistance (`Sd`).

**Formula (Conceptual):**
`P_x = P_e + ( (ΣSd) / Sd_Total ) * (P_i - P_e)`

**Where:**
*   `P_x` = Vapor pressure at a specific point [Pa]
*   `ΣSd` = Sum of `Sd` values from the exterior up to that point [m]
*   `Sd_Total` = Total vapor resistance of the wall (5.77 m)

#### Step 5: Compliance Check - The Graphical Method

The final and most critical step is to compare the **Saturation Vapor Pressure (`P_sat`)** and the **Actual Vapor Pressure (`P`)** at every point in the wall.

*   **Saturation Pressure Line:** Calculated from the temperature distribution (Step 3) using the Magnus formula. This line represents the *maximum* amount of vapor the air can hold at each temperature.
*   **Vapor Pressure Line:** Calculated from the vapor diffusion (Step 4). This line represents the *actual* amount of vapor present.

**Compliance Criterion (Page 88 & 154):**
> "If any of the vapor pressure values reaches or exceeds the saturation vapor pressure at that point, condensation will occur."

**Result for the Example Wall (Page 89 & 155):**
The document presents a graph showing that the two lines (**P_sat** and **P**) **do not intersect** at any point through the wall's cross-section.

**Conclusion:** "For the established exterior (January) and interior conditions, **no interstitial condensation** occurs in any of the layers that form the analyzed enclosure."

### Summary

The document demonstrates a complete, code-compliant check for interstitial condensation:
1.  **Defines** the wall's thermal and hygric properties.
2.  **Establishes** the worst-case realistic interior and exterior environmental conditions.
3.  **Calculates** the temperature and vapor pressure profile through the wall.
4.  **Verifies** that the vapor pressure remains below the saturation pressure everywhere, thus proving no risk of harmful interstitial condensation for the analyzed assembly.