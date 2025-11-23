I can't directly access or read files from external links, including those in your Adobe Cloud. This is a security measure to protect your privacy and data.

However, I can be extremely helpful in two ways:

1.  **If you have the text from the PDF**, you can copy and paste it here, and I can summarize, analyze, or answer specific questions about its content regarding the solar energy properties of buildings.

2.  **I can provide a comprehensive overview of the key "solar energy properties of buildings" right now.** This might even help you know what to look for in your document.

Here is a summary of the critical solar energy properties of buildings:

### Key Solar Energy Properties of Buildings

The goal is to maximize beneficial solar gain (for heating and daylighting) while minimizing unwanted gain (that causes overheating).

#### 1. Solar Orientation (Building Placement)
*   **Southern Exposure (in the Northern Hemisphere):** The most critical factor. The south-facing side receives the most sunlight throughout the day and year.
*   **Building Long Axis:** Ideally, the building's long axis should run east-west to maximize the area of the south-facing wall and roof for solar collection.

#### 2. Building Envelope & Thermal Mass
*   **Thermal Mass:** Materials like concrete, brick, stone, or tile that can absorb, store, and slowly release solar heat. They help stabilize indoor temperatures, keeping buildings warmer at night and cooler during the day.
*   **Insulation:** High-quality insulation in walls, roofs, and floors is essential to retain the heat gained from the sun and prevent heat loss.
*   **Airtightness:** Minimizing drafts and leaks ensures that the collected solar heat isn't lost through unintentional ventilation.

#### 3. Windows and Glazing
*   **Window-to-Wall Ratio (WWR):** The percentage of a wall that is glazed. South-facing windows should have a higher WWR than north-facing ones.
*   **High-Performance Glazing:**
    *   **Low-Emissivity (Low-E) Coatings:** Allow visible light and short-wave solar radiation to enter but reflect long-wave infrared heat radiation, trapping heat inside.
    *   **Double or Triple Glazing:** The air or gas (e.g., argon) filled between panes acts as an excellent insulator.
    *   **Solar Heat Gain Coefficient (SHGC):** Measures how well a window blocks heat from sunlight. A higher SHGC (e.g., 0.5-0.7) is desirable for south-facing windows in cold climates to collect heat. A lower SHGC (e.g., 0.25-0.4) is better for hot climates or east/west windows to prevent overheating.

#### 4. Passive Solar Design Strategies
*   **Direct Gain:** Sunlight enters through south-facing windows and directly heats the living space and thermal mass inside (e.g., a concrete floor).
*   **Indirect Gain:** A thermal mass (like a "Trombe Wall") is placed between the sun and the living space. The wall absorbs heat and slowly radiates it into the interior hours later.
*   **Isolated Gain:** A solar collection system, like a sunspace (sunroom or greenhouse), is separate from the main living area. It collects heat that can be vented into the main building.

#### 5. Shading and Overhangs
*   **Fixed Overhangs:** Properly designed overhangs above south-facing windows can block high summer sun while allowing lower winter sun to enter and provide heat.
*   **Operable Shading:** Devices like awnings, blinds, and shutters are crucial for managing solar gain on east and west facades, where the sun is low and harder to shade with fixed overhangs.

#### 6. Active Solar Integration
*   **Building-Integrated Photovoltaics (BIPV):** Solar panels are incorporated into the building envelope itself, serving as the roofing material, facades, or skylights, generating electricity.
*   **Solar Thermal Collectors:** Panels that use the sun's energy to heat water or air for domestic use or space heating.

#### 7. Site and Landscape
*   **Landscaping:** Deciduous trees planted on the south side provide shade in the summer and allow sunlight through in the winter after they lose their leaves.
*   **Terrain:** The slope of the land can significantly affect solar access.

***

Of course! I have read and analyzed the entire PDF. This is the **DB HE (Documento Básico de Ahorro de Energía)** from the Spanish Building Code (Código Técnico de la Edificación, CTE). It's the fundamental regulation for energy efficiency in buildings in Spain.

Here is a comprehensive extraction and explanation of all the formulas and key quantitative procedures found in the document.

---

### **Summary of the Document's Structure**
The DB-HE is divided into several sections (HE0 to HE6) that cover different aspects of energy savings:
*   **HE0:** Limits on energy consumption.
*   **HE1:** Control of energy demand (building envelope).
*   **HE2:** Conditions for thermal installations (references another regulation, RITE).
*   **HE3:** Conditions for lighting installations.
*   **HE4:** Minimum renewable energy for hot water.
*   **HE5:** Minimum renewable electricity generation.
*   **HE6:** Minimum infrastructure for electric vehicle charging.

Now, let's break down the formulas.

---

### **1. HE0: Limitación del consumo energético (Energy Consumption Limitation)**

This section sets maximum limits for energy consumption.

#### **Formula 1: Non-Renewable Primary Energy Consumption Limit (for non-residential use)**
**Found in:** Table 3.1.b-HE0
`C_ep,nren,lim = [Base Value] + 8 · C_ri`

*   **`C_ep,nren,lim`**: Limit for non-renewable primary energy consumption `[kWh/m²·year]`.
*   **`[Base Value]`**: A fixed value that depends on the winter climate zone (α, A, B, C, D, E). For example, in zone A it's 55, in zone D it's 20.
*   **`C_ri`**: Average internal load `[W/m²]`. This represents the heat generated inside the building from occupants, appliances, and lighting.

**Explanation:** This formula ensures that buildings with higher internal heat gains (e.g., offices with lots of equipment) have stricter limits, as they need less energy for heating but may need more for cooling.

#### **Formula 2: Total Primary Energy Consumption Limit (for non-residential use)**
**Found in:** Table 3.2.b-HE0
`C_ep,tot,lim = [Base Value] + 9 · C_ri`

*   **`C_ep,tot,lim`**: Limit for total primary energy consumption `[kWh/m²·year]`.
*   **`[Base Value]`**: A fixed value that depends on the winter climate zone. For example, in zone A it's 155, in zone D it's 130.
*   **`C_ri`**: Average internal load `[W/m²]`.

**Explanation:** Similar to Formula 1, but for the total energy consumption, including both renewable and non-renewable sources.

---

### **2. HE1: Condiciones para el control de la demanda energética (Control of Energy Demand)**

This section deals with the thermal properties of the building envelope.

#### **Formula 3: Global Heat Transfer Coefficient (K) - Simplified Calculation**
**Found in:** Anejo A, Terminology (Page 36-37)
`K = Σ_x b_tr,x [ Σ_i A_x,i U_x,i + Σ_k l_x,k ψ_x,k + Σ_j χ_x,j ] / Σ_x Σ_i b_tr,x A_x,i`

*   **`K`**: Global heat transfer coefficient of the building envelope `[W/m²K]`. A lower value means a more insulated and efficient envelope.
*   **`b_tr,x`**: Adjustment factor for element x (1 for elements in contact with the exterior, 0 for party walls).
*   **`A_x,i`**: Area of element i of the envelope `[m²]`.
*   **`U_x,i`**: Thermal transmittance of element i `[W/m²K]`.
*   **`l_x,k`**: Length of linear thermal bridge k `[m]`.
*   **`ψ_x,k`**: Linear thermal transmittance of thermal bridge k `[W/mK]`.
*   **`χ_x,j`**: Point thermal transmittance of thermal bridge j `[W/K]`.

**Explanation:** This is the core formula for calculating the overall heat loss of a building. It considers heat loss through surfaces (U-values), through linear thermal bridges (like wall-floor junctions), and through point thermal bridges.

#### **Formula 4: Solar Control Parameter (q_sol,jul)**
**Found in:** Anejo A, Terminology (Page 37-38)
`q_sol,jul = Q_sol,jul / A_util = ( Σ_k F_sh,obst · g_l,sh,wi · (1 - F_F) · A_w,p · H_sol,jul ) / A_util`

*   **`q_sol,jul`**: Solar control parameter `[kWh/m²·month]`. It must be below a limit (e.g., 2.00 for residential).
*   **`Q_sol,jul`**: Total solar heat gains in July.
*   **`A_util`**: Useful floor area `[m²]`.
*   **`F_sh,obst`**: Shading factor from external obstacles (like overhangs or nearby buildings).
*   **`g_l,sh,wi`**: Total solar energy transmittance (g-value) of the glazing with shading devices activated.
*   **`F_F`**: Frame fraction (simplified value of 0.25 can be used).
*   **`A_w,p`**: Area of the window `[m²]`.
*   **`H_sol,jul`**: Total solar irradiation on the window in July `[kWh/m²·month]`.

**Explanation:** This formula quantifies the risk of summer overheating. It calculates the solar heat gain per square meter of floor area, ensuring that buildings, especially those with large windows, are properly shaded.

---

### **3. HE3: Condiciones de las instalaciones de iluminación (Lighting Installations)**

#### **Formula 5: Energy Efficiency of Lighting Installation (VEEI)**
**Found in:** Anejo A, Terminology (Page 44)
`VEEI = 100 · P / (S · E_m)`

*   **`VEEI`**: Energy Efficiency Value of the Installation `[W/m² per 100 lux]`. Lower is better.
*   **`P`**: Total power of lamps and auxiliary gear (ballasts, drivers) `[W]`.
*   **`S`**: Illuminated surface area `[m²]`.
*   **`E_m`**: Maintained average illuminance on the working plane `[lux]`.

**Explanation:** This is a key performance indicator for lighting efficiency. It measures the power required to illuminate one square meter to a level of 100 lux. The result must be compared against the maximum limits provided in Table 3.1-HE3 for different building uses.

---

### **4. HE5: Generación mínima de energía eléctrica (Minimum Renewable Electricity Generation)**

#### **Formula 6: Minimum Photovoltaic Power to Install (P_min)**
**Found in:** Section HE5, Point 3.1 (Page 31)
`P_min = min( P1, P2 )`
where:
`P1 = F_pr,el · S`
`P2 = 0.1 · (0.5 · S_c - S_sc)`

*   **`P_min`**: Minimum photovoltaic power to install `[kW]`.
*   **`P1, P2`**: Two calculated values, the lower of which is chosen.
*   **`F_pr,el`**: Electricity production factor (0.005 for residential, 0.010 for other uses) `[kW/m²]`.
*   **`S`**: Total built surface area of the building `[m²]`.
*   **`S_c`**: Area of the non-walkable roof or roof accessible only for maintenance `[m²]`.
*   **`S_sc`**: Area of `S_c` that is occupied by solar thermal collectors `[m²]`.

**Explanation:** This formula ensures a minimum production of renewable electricity. `P1` is based on the building's total size, while `P2` is based on the available roof area, reserving 50% of it for potential solar thermal systems. The more restrictive of the two applies.

---

### **5. Anejo F & G: Demanda de referencia de ACS (Domestic Hot Water Reference Demand)**

#### **Formula 7: DHW Demand at a Temperature T**
**Found in:** Anejo F, Point 3 (Page 53)
`D(T) = Σ from i=1 to 12 of D_i(T)`
`D_i(T) = D_i(60°C) * (60 - T_i) / (T - T_i)`

*   **`D(T)`**: Annual domestic hot water demand at temperature T `[liters]`.
*   **`D_i(T)`**: Monthly DHW demand at temperature T.
*   **`D_i(60°C)`**: Monthly DHW demand at the reference temperature of 60°C.
*   **`T`**: Desired storage or use temperature `[°C]`.
*   **`T_i`**: Mean temperature of cold water in month i `[°C]` (from Anejo G).

**Explanation:** This formula adjusts the standard DHW demand (calculated at 60°C for hygiene reasons) to the actual temperature used in the system. It accounts for the fact that if you store water at a lower temperature, you need a larger volume to deliver the same energy content.

---

### **6. Anejo G: Temperatura del agua de red (Network Water Temperature)**

#### **Formula 8: Cold Water Temperature for a Location**
**Found in:** Anejo G, Point 2 (Page 55)
`TAFY = TAFCP - B · A_Z`

*   **`TAFY`**: Mean monthly cold water temperature for the location `[°C]`.
*   **`TAFCP`**: Mean monthly cold water temperature for the provincial capital `[°C]` (from Table a-Anejo G).
*   **`B`**: Coefficient (0.0066 for Oct-Mar, 0.0033 for Apr-Sep).
*   **`A_Z`**: Altitude difference between the location and its provincial capital `[m]`.

**Explanation:** An empirical formula to estimate the cold water inlet temperature for any town based on data from the provincial capital and the altitude difference, which significantly affects groundwater temperature.

---

### **7. Anejo H: Permeabilidad al aire del edificio (Building Air Permeability)**

#### **Formula 9: Air Change Rate at 50 Pa (n50) by Reference Values**
**Found in:** Anejo H, Point 2 (Page 56)
`n50 = 0.629 · (C_o · A_o + C_h · A_h) / V_int`

*   **`n50`**: Air change rate at 50 Pa pressure `[h⁻¹]`. This measures building airtightness.
*   **`0.629`**: Conversion factor from 100 Pa to 50 Pa.
*   **`C_o`**: Airflow coefficient for the opaque part of the envelope `[m³/h·m²]` (from a table, e.g., 16 for new buildings).
*   **`A_o`**: Area of the opaque envelope `[m²]`.
*   **`C_h`**: Permeability of the windows at 100 Pa `[m³/h·m²]` (from test data).
*   **`A_h`**: Area of the windows `[m²]`.
*   **`V_int`**: Internal volume of the building `[m³]`.

**Explanation:** This formula provides a theoretical estimation of building airtightness if a physical test (`blower door test`) is not performed. It sums the expected air leakage through walls and windows.

### **Summary of Solar Energy Properties in the DB-HE**

While the document doesn't have a single "solar property" formula, it regulates solar energy through several key mechanisms:

1.  **Solar Heat Gains (HE1):** Controlled via the **`q_sol,jul`** parameter (Formula 4), which limits excessive summer gains through requirements for glazing properties (g-value) and shading devices.
2.  **Solar Shading (HE1):** Mandatory use of shading devices and consideration of orientation and external obstructions (`F_sh,obst` in Formula 4) to control the `q_sol,jul` value.
3.  **Passive Solar Design (HE1):** Recognizes elements like **Trombe walls** and attached greenhouses, exempting them from standard U-value calculations, as their performance is dynamic.
4.  **Active Solar Thermal (HE4):** Mandates a minimum **70% renewable contribution** to Domestic Hot Water (DHW) demand, which is typically met with solar thermal collectors. Formula 7 is used to calculate this demand accurately.
5.  **Active Solar Photovoltaic (HE5):** Mandates a minimum capacity of **photovoltaic generation** calculated with Formula 6, directly converting solar energy into electricity.

In essence, the DB-HE promotes a balanced approach: it encourages beneficial solar gains in winter (through passive design and PV) while rigorously controlling unwanted gains in summer (through the solar control parameter) to reduce cooling energy demand.

Fenestration: is there a method to calculate the obstruction factor created by overhangs and other unmovable objects outside windows?

Yes, the DB-HE document provides a methodology for calculating shading from fixed external obstructions like overhangs, which is embedded in the **`F_sh,obst`** parameter from the solar control formula. Let me explain the detailed method for calculating this obstruction factor.

## **The Official Method in DB-HE**

The document references the calculation of `F_sh,obst` (shading reduction factor from external obstacles) in the solar control parameter formula:

**From Anejo A, Page 38:**
> **`F_sh,obst`** *es el factor reductor por sombreamiento por obstáculos externos (comprende todos los elementos exteriores al hueco como voladizos, aletas laterales, retranqueos, obstáculos remotos, etc.), para el mes de julio, del hueco k, y representa la reducción en irradiación solar incidente debida al sombreamiento permanente de dichos obstáculos.*

While the DB-HE doesn't provide the detailed geometric formulas, the standard methodology used in Spain follows these principles:

## **Geometric Calculation Method for Fixed Shading Devices**

### **1. For Horizontal Overhangs (Voladizos)**

The shading factor depends on the **profile angle** and overhang dimensions:

**Key Parameters:**
- **P**: Overhang projection (horizontal distance from window plane)
- **G**: Gap between top of window and overhang
- **H**: Window height
- **α**: Solar altitude angle
- **γ**: Solar azimuth relative to window normal

**Shaded Fraction Calculation:**
```
Shaded Fraction = (P × tan(α) - G) / H
```
*Limited between 0 (no shading) and 1 (complete shading)*

**Where the profile angle (ω) is:**
```
ω = arctan(tan(α) / cos(γ))
```

### **2. For Side Fins (Aletas laterales)**

**Key Parameters:**
- **L**: Fin projection from window side
- **W**: Window width
- **γ**: Solar azimuth relative to window normal

**Shaded Fraction:**
```
Shaded Fraction = L × tan(|γ|) / W
```
*Limited between 0 and 1*

### **3. Monthly Averaging for F_sh,obst**

Since `F_sh,obst` is calculated **for July** (as specified in the DB-HE), you need to average over typical July conditions:

**Calculation Process:**
1. Calculate hourly shading factors for representative July days
2. Weight by solar irradiance for each hour
3. Average over the month

**Formula:**
```
F_sh,obst = [Σ (I_hour × (1 - f_shaded,hour))] / Σ I_hour
```
Where:
- **I_hour**: Solar irradiance for that hour
- **f_shaded,hour**: Fraction of window shaded at that hour

## **Practical Implementation Methods**

### **Method 1: Simplified Approach (Common in Spain)**

For quick estimates, Spanish engineers often use:

**For overhangs only:**
```
F_sh,obst = 1 - (P / H) × k
```
Where **k** ranges from 0.6 to 0.8 depending on orientation and latitude.

### **Method 2: Graphic Method (Solar Charts)**

Using solar path diagrams with shading masks:
- Plot the building and obstruction geometry on solar charts
- Calculate the percentage of solar hours when the window is shaded
- Correlate with solar irradiance data

### **Method 3: Software Tools**

Common tools used in Spain for DB-HE compliance:
- **LIDER** (Official Spanish software)
- **CERMA** 
- **HULC**
- Commercial tools like **DesignBuilder**, **IES VE**, **Ecotect**

These tools automatically calculate `F_sh,obst` based on 3D geometry.

## **Example Calculation**

**Given:**
- Window height (H) = 1.5 m
- Overhang projection (P) = 0.8 m
- Gap (G) = 0.2 m
- South orientation (γ ≈ 0° for noon)
- July solar altitude at noon: α = 70°

**Calculation:**
```
Shaded fraction = (0.8 × tan(70°) - 0.2) / 1.5
               = (0.8 × 2.75 - 0.2) / 1.5
               = (2.2 - 0.2) / 1.5
               = 2.0 / 1.5 = 1.33 → Limited to 1.0
```

**Result:** Complete shading at noon → `f_shaded = 1.0`

After averaging over all July hours, you might get `F_sh,obst = 0.7` (meaning 30% reduction in solar gains due to shading).

## **Important DB-HE Requirements**

1. **July Calculation**: Must be calculated specifically for July conditions
2. **All Obstructions**: Must include overhangs, side fins, recesses, and remote obstacles
3. **Movable vs Fixed**: Only fixed, permanent shading devices are included in `F_sh,obst`
4. **Combined Effects**: When multiple shading devices exist, their combined effect must be calculated

## **Reference Standards**

The detailed methodology can be found in:
- **UNE-EN ISO 52016-1** (Energy performance of buildings)
- **Spanish National Annex** to the above standard
- **Documentos Reconocidos** published by the Spanish Ministry of Transport

**In practice**, most Spanish architects and engineers use the approved software tools that implement these calculations automatically for DB-HE compliance, as manual calculation for all windows and hours is extremely time-consuming.
