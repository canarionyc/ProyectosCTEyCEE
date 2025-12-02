# Summary of the CTE DB-HE 2019 Application Guide

This document summarizes the application guide for the Basic Document on Energy Saving (DB-HE) of the Technical Building Code (CTE). It establishes the requirements for buildings to achieve reduced energy consumption, largely covered by renewable sources .

## HE0: Limitation of Energy Consumption

This section limits the Total Primary Energy Consumption ($C_{ep,tot}$) and Non-Renewable Primary Energy Consumption ($C_{ep,nren}$) to mitigate climate change and reduce energy dependency .

### 1. General Calculation Concepts
The final energy consumption depends on the demand and the efficiency of the systems:
$$C_{final} = \frac{\text{Energy Demand}}{\text{Mean System Efficiency } (\eta)}$$


### 2. Internal Heat Load (CFI)
For tertiary use buildings, the limit of consumption depends on the internal load, calculated for a standard week:
$$CFI = \frac{\sum C_{oc}}{7 \cdot 24} + \frac{\sum C_{il}}{7 \cdot 24} + \frac{\sum C_{eq}}{7 \cdot 24}$$
* **$C_{oc}$**: Sensible load from occupancy .
* **$C_{il}$**: Load from lighting .
* **$C_{eq}$**: Load from equipment .
* The result is averaged over $168$ hours (7 days $\times$ 24 hours) .

### 3. Key Parameters and Limits
* **Export Factor ($k_{exp}$):** For standard verification, $k_{exp} = 0$, meaning exported energy is not deducted from consumption .
* **Consumption Limits ($C_{ep,lim}$):**
    * **Residential ($C_{ep,nren}$):** Ranges from **20** (Zone $\alpha$) to **43** (Zone E) $kWh/m^2\cdot year$ for new buildings .
    * **Residential ($C_{ep,tot}$):** Ranges from **40** (Zone $\alpha$) to **86** (Zone E) $kWh/m^2\cdot year$ for new buildings .
    * **Tertiary:** Limits are calculated as a base value plus a factor of CFI (e.g., Zone D: $20 + 8 \cdot CFI$) .

---

## HE1: Conditions for Energy Demand Control

This section ensures the quality of the thermal envelope to minimize energy demand for heating and cooling .



[Image of building thermal envelope diagram]


### 1. Global Heat Transmission Coefficient ($K$)
The weighted average of thermal transmittance of the envelope, including thermal bridges :
$$K = \frac{\sum H_x}{A_{int}} = \frac{\sum b_{tr,x} [\sum A_{x,i} U_{x,i} + \sum l_{x,k} \psi_{x,k} + \sum \chi_{x,j}]}{\sum b_{tr,x} A_{x,i}}$$
* **$H_x$**: Heat transfer coefficient of element $x$ .
* **$A_{int}$**: Total thermal exchange area .
* **$b_{tr,x}$**: Adjustment factor (1 for exterior, 0 for adjacent buildings) .
* **$U_{x,i}$**: Thermal transmittance of the element .
* **$\psi_{x,k}$**: Linear thermal transmittance of thermal bridges .

### 2. Air Permeability ($n_{50}$)
This formula estimates the air change rate at 50 Pa pressure (mandatory for new residential buildings $>120 m^2$) :
$$n_{50} = 0.629 \cdot \frac{(C_o \cdot A_o + C_h \cdot A_h)}{V_{int}}$$
* **$C_o$**: Flow coefficient for opaque elements ($16$ for new, $29$ for existing) .
* **$C_h$**: Flow coefficient for openings (from test data) .
* **$A_o, A_h$**: Areas of opaque and opening elements .
* **$V_{int}$**: Internal air volume .

### 3. Thermal Resistance of Adjacent Spaces ($R_u$)
For modeling unconditioned spaces (like attics) as a homogeneous layer :
$$R_u = \frac{A_i}{\sum (A_{e;k} \cdot U_{e;k}) + 0.33 \cdot n \cdot V_k}$$
* **$A_i$**: Surface area between interior and unconditioned space .
* **$A_{e;k}$**: Surface area between unconditioned space and exterior .
* **$U_{e;k}$**: Transmittance of the external element .
* **$n$**: Ventilation rate of the unconditioned space .

### 4. Solar Control ($q_{sol;jul}$)
Limits the solar gains in July to prevent overheating:
* **Residential:** Limit $\le 2.00 \, kWh/m^2\cdot month$ .
* **Tertiary:** Limit $\le 4.00 \, kWh/m^2\cdot month$ .

---

## HE2: Conditions for Thermal Installations

This section mandates compliance with the **Regulation of Thermal Installations in Buildings (RITE)** to ensure efficiency, comfort, and safety . While specific formulas are contained within the RITE, the guide emphasizes:
* Use of efficient generation equipment .
* Insulation of distribution networks .
* System regulation and control (e.g., temperature ranges of 21-25ºC) .

---

## HE3: Conditions for Lighting Installations

Regulates the energy efficiency of artificial lighting installations while ensuring visual comfort .

### 1. Energy Efficiency Value of the Installation (VEEI)
$$VEEI = \frac{100 \cdot P}{S \cdot E_m}$$
* **$P$**: Total installed power (W) including lamps and auxiliary equipment .
* **$S$**: Lit surface area ($m^2$) .
* **$E_m$**: Maintained average illuminance (lux) .

### 2. Parameters and Limits
* **Maximum Power ($P_{max}$):** Limits range from **5 $W/m^2$** (parking) to **25 $W/m^2$** (for $E > 600$ lux) .
* **$VEEI_{lim}$:** Specific limits by usage, e.g., **3.0** for administrative/offices, **4.0** for classrooms/hospitals, **10.0** for hotel rooms .

---

## HE4: Minimum Renewable Energy for DHW

Requires a percentage of Domestic Hot Water (DHW) demand to be covered by renewable sources .

### 1. DHW Energy Demand (Approximation)
$$D_{ACS} = V_{ACS} \cdot C_{H2O} \cdot \rho_{H2O} \cdot (60^\circ - T_{\text{water network}})$$


### 2. Heat Pump Performance (SCOP)
For a heat pump to be considered renewable for HE4 compliance:
* **$SCOP_{dhw} \ge 2.5$** (Electrically driven heat pumps) .
* **$SCOP_{dhw} \ge 1.15$** (Thermally driven heat pumps) .

### 3. Contribution Parameters
* **Contribution Requirement:**
    * **60%** renewable contribution if demand $< 5000 \, l/d$ .
    * **70%** renewable contribution if demand $> 5000 \, l/d$ .
* **Residual Energy Limit:** A maximum of **20%** of extracted energy can be counted as contribution for residential use .

---

## HE5: Minimum Electrical Energy Generation

Mandates renewable electricity generation (typically Photovoltaic) for buildings with a constructed area $>1000 m^2$ .



[Image of photovoltaic solar panel system]


### 1. Minimum Power to Install ($P_{min}$)
The installed power must be the **lesser** of $P_1$ and $P_2$:
$$P_1 = F_{pr,el} \cdot S$$
$$P_2 = 0.1 \cdot (0.5 \cdot SC - SOC)$$


### 2. Calculation Parameters
* **$S$**: Constructed surface area of the building .
* **$SC$**: Non-trafficable roof surface area .
* **$SOC$**: Roof area occupied by solar thermal collectors .
* **$F_{pr,el}$ (Production Factor):**
    * **0.005** for private residential use .
    * **0.01** for other uses .

---

## HE6: EV Charging Infrastructure

Establishes minimum endowments for electric vehicle charging stations in building parking lots .

### 1. Required Endowments
* **Pre-installation (Cable Conduits):**
    * **100%** of spaces for private residential buildings .
    * **20%** of spaces for other uses .
* **Charging Stations (Private Non-Residential):**
    * **1 station per 40 spaces** (general rule) .
    * **1 station per 20 spaces** (public administration buildings) .
    * **Accessible Stations:** 1 station per 50 accessible spaces (or fraction) .