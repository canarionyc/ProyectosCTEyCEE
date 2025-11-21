# DHW Demand Calculation (`Demanda de ACS`)

The ACS system is a mixed system, sharing the biomass boiler with the heating system and using an accumulation tank.

This calculates the daily volume of hot water needed, including distribution losses.

**Formula:**
`Daily ACS Demand (l/day) = Number of Occupants × Daily Needs per Person (l/p·day)`

**Where:**
*   **Number of Occupants:** Based on DB HE Annex F, Table a (Minimum occupancy for private residential use).
*   **Daily Needs per Person:** Fixed at **28 l/p·day** (at 60°C).

**Option 2: 2 Bedrooms, 3 Occupants**
*   **Base Demand:** `3 occupants × 28 l/p·day = 84 l/day`
*   **Distribution Losses (estimated at 5%):** `84 l/day × 0.05 = 4.2 l/day`
*   **Total Daily Demand (excluding tank losses):** `84 + 4.2 = 88.2 l/day`

[//]: # (**Option 3: 3 Bedrooms, 4 Occupants**)

[//]: # (*   **Base Demand:** `4 occupants × 28 l/p·day = 112 l/day`)

[//]: # (*   **Distribution Losses &#40;estimated at 5%&#41;:** `112 l/day × 0.05 = 5.6 l/day`)

[//]: # (*   **Total Daily Demand &#40;excluding tank losses&#41;:** `112 + 5.6 = 117.6 l/day`)

---

## Heat Loss Calculation for the Accumulation Tank (`Pérdidas en depósito`)

This is a critical calculation to determine the total energy demand, as it includes losses from the hot water storage tank.

`Q = A · U · DeltaT · Number of hours in the period`

**Simplified using the Tank Loss Coefficient:**
`Monthly Losses (Wh) = Loss Coefficient (W/°C) × DeltaT (°C) × Hours in Month`

**Where:**
*   **Loss Coefficient (A·U):** Provided in the system specs.
    *   Options 1 & 2 (100L tank): `0.5 W/°C`
    *   Option 3 (150L tank): `0.8 W/°C`
*   **DeltaT:** Temperature difference between tank interior (65°C) and ambient (20°C) = **45°C**

**Calculation for Option 2:**
*   **For January (744 hours):** `Q_jan = 0.5 W/°C × 45°C × 744 h = 16,740 Wh = 16.74 kWh`
*   **Total Annual Tank Losses:** `197.10 kWh/year`
*   **Average Daily Tank Losses:** `197,100 Wh/year / 365 days = 540 Wh/day`

---

## Equivalent Daily Volume of Tank Losses

This converts the energy lost from the tank back into an equivalent volume of water that would need to be heated.

**Formula:**
`Equivalent Volume (l/day) = Daily Energy Loss (Wh/day) / [DeltaT × C_a × ρ_a]`

**Where:**
*   **DeltaT:** Temperature rise (60°C - T_cold). `T_cold` is the annual average cold water temperature at the project altitude.
*   **C_a:** Specific heat capacity of water = **1.163 Wh/(kg·K)**
*   **ρ_a:** Density of water ≈ **1 kg/l**

**Calculation for Option 2:**
*   Daily Energy Loss = `540 Wh/day`
*   DeltaT = `60°C - 9.74°C = 50.26°C` (9.74°C is the average cold water temp for the location)
*   **Equivalent Volume =** `540 Wh/day / (50.26 °C × 1.163 Wh/(kg·K) × 1 kg/l) ≈ 9.2 l/day`

**Total Demand for HE4 Applicability Check (Option 2):**
*   `88.2 l/day + 9.2 l/day = 97.4 l/day`
*   Since this is **below 100 l/day**, Option 2 is **not subject** to the HE4 renewable contribution requirement.

---

## Total Annual Energy Demand for ACS (`Demanda energética anual`)

This calculates the total energy required to heat the water and compensate for all losses over a year.

**Formula:**
`Monthly ACS Energy (kWh) = V_ACS_month (l) × C_a × ρ_a × (60°C - T_cold_month) / 1000`

**Where:**
*   `V_ACS_month` is the monthly volume of water used (at 60°C).
*   `T_cold_month` is the monthly average cold water temperature.

**Calculation for Option 3:**
*   Based on detailed month-by-month calculation.
*   **Total Annual Energy Demand (including tank losses):** `2,823.00 kWh/year`
*   **Useful Floor Area (Option 3):** `128 m²`
*   **Specific Demand:** `2,823.00 kWh/year / 128 m² = 22.05 kWh/m²·year`

---

## Renewable Energy Contribution Calculation (`Contribución renovable`)

This proves compliance with HE4, showing that over 60% of the ACS demand is met by renewable energy (biomass).

**Step-by-Step Calculation:**

**Step 1: Final Energy Consumption**
*   **Formula:** `Final Energy (kWh/m²·year) = ACS Demand (kWh/m²·year) / Boiler Efficiency`
*   **Calculation:** `22.05 kWh/m²·year / 0.93 = 23.71 kWh/m²·year`

**Step 2: Calculate Renewable Portion of Final Energy**
*   **Formula:** `Renewable Final Energy = Final Energy × (f_ep,ren / f_ep,tot)`
*   **Factors for Biomass Pellets:**
    *   `f_ep,ren` = 1.028
    *   `f_ep,tot` = 1.113
*   **Ratio:** `1.028 / 1.113 = 0.9236`
*   **Calculation:** `23.71 kWh/m²·year × 0.9236 = 21.90 kWh/m²·year`

**Step 3: Convert Back to Renewable Demand**
*   **Formula:** `Renewable Demand = Renewable Final Energy × Boiler Efficiency`
*   **Calculation:** `21.90 kWh/m²·year × 0.93 = 20.37 kWh/m²·year`

**Step 4: Calculate Renewable Percentage**
*   **Formula:** `% Renewable = (Renewable Demand / Total ACS Demand) × 100`
*   **Calculation:** `(20.37 / 22.05) × 100 = 92.4%`

**Compliance Check (HE4):**
*   **Requirement for demand < 5000 l/day:** Minimum **60%** renewable contribution.
*   **Result:** `92.4% > 60%` **COMPLIES**

## Summary of ACS System Data:

| Aspect | Option 2 | Option 3 |
| :--- | :--- | :--- |
| **Occupants / Bedrooms** | 3 / 2 | 4 / 3 |
| **Daily Demand (w/ distribution losses)** | 88.2 l/day | 117.6 l/day |
| **Accumulator Volume** | 100 L | 150 L |
| **Tank Loss Coefficient (A·U)** | 0.5 W/°C | 0.8 W/°C |
| **Total Demand (w/ tank losses)** | 97.4 l/day | (N/A, calculated in kWh) |
| **HE4 Applicable?** | **No** (<100 l/day) | **Yes** (>100 l/day) |
| **Specific Annual Demand** | (Not fully calculated) | **22.05 kWh/m²·year** |
| **Renewable Contribution** | (Not required) | **92.4%** |

The document provides a complete traceability from the basic water consumption needs to the final proof that the system, powered by a biomass boiler, comfortably exceeds the legal requirements for renewable energy use in domestic hot water production.