
# Air Permeability of Openings (`Permeabilidad al aire de los huecos`)

The document addresses air tightness in two key areas: the individual components (windows/doors) and the entire building envelope.

This regulates the maximum allowed air leakage through windows, doors, and skylights under a standardized pressure test.

**Standard:** UNE-EN 12207:2017
**Test Condition:** Air permeability measured at a pressure differential of **100 Pa**, denoted as **Q₁₀₀**.
**Unit:** m³/(h·m²) - (cubic meters per hour, per square meter of opening)

## Compliance Table

The following table is used to verify that the proposed window and door classes meet the regulatory limits for the winter climate zone "E".

| Component Type | Orientation / Location | Permeability Class | Q₁₀₀ Value (m³/h·m²) | Limit (Q₁₀₀,lim) (m³/h·m²) | Compliance |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Windows** | North & East Facades | Class 3 | 9 | ≤ 9 | **COMPLIES** |
| **Windows** | South & West Facades | Class 3 | 9 | ≤ 9 | **COMPLIES** |
| **Access Door** | West Facade | (Wood, no class given) | (Not specified) | ≤ 9* | **COMPLIES** * |
| **Skylights** (`Lucernarios`) | Roof | Class 3 | 9 | ≤ 9 | **COMPLIES** |

*The door's specific permeability is not given, but it is stated to comply.

**Key Requirement:** For climate zone E, the permeability of all openings in the thermal envelope must not exceed **9 m³/(h·m²)**. All proposed components with a Class 3 rating meet this requirement.

---

## Building Envelope Air Tightness (`Relación del cambio de aire n₅₀`)

This is a whole-building test that measures the air tightness of the entire thermal envelope, including leaks through walls, junctions, and installation gaps, not just the windows.

**Standard:** UNE-EN 13829:2002 (Fan Pressurization Test / Blower Door Test)
**Test Condition:** Air changes per hour measured at a pressure differential of **50 Pa**, denoted as **n₅₀**.
**Unit:** h⁻¹ (air changes per hour)

### Regulatory Limit

The permissible n₅₀ value depends on the building's compactness (V/A).

**Table 3.1.3.b-HE1**

| Compactness (V/A) [m³/m²] | n₅₀ Limit [h⁻¹] |
| :--- | :--- |
| V/A ≤ 2.0 | 6.00 |
| V/A ≥ 4.0 | 3.00 |

*For intermediate compactness values (2 < V/A < 4), the limit is obtained by linear interpolation.*

**Applicability:** This requirement is only mandatory for new residential buildings with a **useful floor area greater than 120 m²**.

### Calculation of Permeability (`n₅₀`)

The document provides a method for calculating the n₅₀ value without performing a test, using reference values.

**Formula:**
`n₅₀ = 0.629 × (C_o × A_o + C_h × A_h) / V`

**Where:**
*   **`n₅₀`**: The calculated air change rate at 50 Pa [h⁻¹].
*   **`0.629`**: Conversion factor between permeability at 100 Pa (Q₁₀₀) and 50 Pa (n₅₀).
*   **`C_o`**: Airflow coefficient for the **opaque** part of the envelope at 100 Pa. For new buildings, this is **16 m³/(h·m²)**.
*   **`A_o`**: Area of the **opaque** part of the thermal envelope [m²].
*   **`C_h`**: Airflow coefficient for the **openings** (windows, doors) at 100 Pa. This is equal to their Q₁₀₀ value. For Class 3 components, this is **9 m³/(h·m²)**.
*   **`A_h`**: Total area of the **openings** (windows, doors) in the thermal envelope [m²].
*   **`V`**: Internal air volume enclosed by the thermal envelope (`Volumen de "aire interior"`) [m³].

### Application and Compliance in the Document

The document states that due to the small size of the building, the n₅₀ requirement only applies to **Option 3**, which has a useful area of 128 m² (>120 m²).

*   **For Options 1 & 2:** The useful area is less than 120 m², so justifying the n₅₀ value is **not mandatory**.

*   **Compliance Strategy for Option 3:**
    The document mentions that achieving compliance for small, detached buildings can be challenging. For Option 3, compliance is achieved by specifying even tighter **Class 4 windows** (Q₁₀₀ ≤ 3 m³/(h·m²)) to compensate for the less favorable compactness.

    > "*...this requirement only applies in option 3 (> 120 m² useful) and compliance is achieved by improving the tightness of the openings by incorporating Class 4 carpentry, which guarantees less than 3 m³/h·m².*"

## Summary of Air Tightness Data:

| Aspect | Requirement / Value | Notes |
| :--- | :--- | :--- |
| **Openings (Q₁₀₀)** | **Limit: ≤ 9 m³/(h·m²)** | For climate zone E. |
| **Openings Class** | **Class 3** | Standard proposed for most options. |
| **Openings for Compliance** | **Class 4** | Proposed for Option 3 to meet n₅₀. |
| **Building (n₅₀)** | **Limit: Function of Compactness** | See table above. |
| **n₅₀ Applicability** | **Only for > 120 m² useful area** | Only mandatory for Option 3. |
| **Calculation Method** | `n₅₀ = 0.629 × (16·A_o + 9·A_h) / V` | For a standard case with Class 3 windows. |
| **Opaque Coefficient (C_o)** | **16 m³/(h·m²)** | For new buildings. |

In conclusion, the document demonstrates a two-tiered approach to air tightness: ensuring all individual components meet a minimum standard (Class 3), and for larger buildings, using higher-performance components (Class 4) to ensure the whole-building envelope meets the more stringent n₅₀ requirement.