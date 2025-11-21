[Header 1 ("heating-system", [], []) [Str "Heating System"], Para [Str "The heating system for this single-family home is a biomass pellet boiler that feeds a low-temperature water-based underfloor heating system."], Header 2 ("heating-power-distribution-and-sizing", ["unnumbered", "unlisted"], []) [Str "Heating Power Distribution and Sizing"], Para [Str "This calculation determines the required thermal power output for each room based on the heated surface area and the average emission power of the underfloor heating system."], Para [Strong [Str "Formula:"], SoftBreak, Code ("", [], []) "Heating Power (W) = Surface Area (m²) × Average Emission Power (W/m²)"], BulletList [[Para [Strong [Str "Ground Floor (P02) - Emission Power: 70 W/m²"]], BulletList [[Plain [Str "Kitchen-Dining-Living Room: ", Code ("", [], []) "28.80 m² × 70 W/m² = 2,016 W"]], [Plain [Str "Entrance + Hallway: ", Code ("", [], []) "13.44 m² × 70 W/m² = 941 W"]], [Plain [Str "Toilet: ", Code ("", [], []) "4.14 m² × 70 W/m² = 290 W"]], [Plain [Str "Main Bedroom: ", Code ("", [], []) "17.62 m² × 70 W/m² = 1,233 W"]], [Plain [Strong [Str "Total Ground Floor Power:"], Str " ", Code ("", [], []) "64.00 m² × 70 W/m² = 4,480 W"]]]], [Para [Strong [Str "Attic Floor (P03) - Emission Power: 85 W/m²"]], BulletList [[Plain [Str "Bedroom: ", Code ("", [], []) "29.15 m² × 85 W/m² = 2,478 W"]], [Plain [Str "Toilet: ", Code ("", [], []) "6.85 m² × 85 W/m² = 582 W"]], [Plain [Strong [Str "Total Attic Floor Power:"], Str " ", Code ("", [], []) "36.00 m² × 85 W/m² = 3,060 W"]]]], [Para [Strong [Str "Total Building Heating Power:"], Str " ", Code ("", [], []) "4,480 W + 3,060 W = 7,540 W"]]], HorizontalRule, Header 2 ("final-energy-consumption-for-heating", ["unnumbered", "unlisted"], []) [Str "Final Energy Consumption for Heating"], Para [Str "This calculation converts the heating demand into the actual amount of final energy (biomass pellets) that needs to be purchased, taking the boiler's efficiency into account."], Para [Strong [Str "Formula:"], SoftBreak, Code ("", [], []) "Final Energy Consumption (kWh/m²·year) = Heating Demand (kWh/m²·year) / Boiler Efficiency"], BulletList [[Plain [Str "Heating Demand, D = ", Code ("", [], []) "39.45 kWh/m²·year"]], [Plain [Str "Boiler Nominal Efficiency = ", Code ("", [], []) "93%", Str " or ", Code ("", [], []) "0.93"]], [Plain [Strong [Str "Final Energy Consumption ="], Str " ", Code ("", [], []) "39.45 kWh/m²·year / 0.93 = 42.17 kWh/m²·year"]]], HorizontalRule, Header 2 ("nominal-efficiency-versus-overall-efficiency", ["unnumbered", "unlisted"], []) [Str "Nominal Efficiency versus Overall Efficiency"], Para [Str "The nominal efficiency of the boiler (0.93) is not the same as the overall system efficiency from fuel input to useful heat in the rooms."], Para [Str "The nominal boiler efficiency only accounts for losses within the boiler itself (combustion inefficiency and heat lost through the flue). It does not include other significant losses in the system. Your calculated overall efficiency of ", Str "~", Str "0.75 is entirely plausible and points to these other sources of power loss."], Para [Str "Here are the other sources of power loss for the heated floor system that explain the difference between the boiler's nominal efficiency and the effective system efficiency you calculated:"], Header 4 ("distribution-losses-pérdidas-de-distribución", ["unnumbered", "unlisted"], []) [Str "Distribution Losses (Pérdidas de distribución)"], Para [Str "This is often the most significant loss after the boiler. The pipes that carry hot water from the boiler to the underfloor heating loops (and back) lose heat to their surroundings."], BulletList [[Plain [Strong [Str "Location:"], Str " These pipes often run through unheated spaces like the sanitary crawl space (", Code ("", [], []) "Cámara Sanitaria", Str "), which, as per the document, is a non-habitable space at a much lower temperature."]], [Plain [Strong [Str "Impact:"], Str " Heat that escapes from these pipes warms the crawl space instead of the living areas, constituting a direct loss. While the document's main energy calculation might account for this indirectly through the building's overall heat demand, a detailed system loss calculation would include it explicitly."]], [Plain [Strong [Str "Formula (Conceptual):"], Str " ", Code ("", [], []) "Q_dist_loss = U_pipe * L_pipe * DeltaT * time"], BulletList [[Plain [Code ("", [], []) "U_pipe", Str ": Thermal transmittance of the insulated pipe (W/m·K)."]], [Plain [Code ("", [], []) "L_pipe", Str ": Total length of the distribution pipes in unheated spaces (m)."]], [Plain [Code ("", [], []) "DeltaT", Str ": Difference between average water temperature in the pipe and the temperature of the unheated space (K)."]]]]], Header 4 ("emission--installation-losses-pérdidas-de-emisión", ["unnumbered", "unlisted"], []) [Str "Emission / Installation Losses (Pérdidas de emisión)"], Para [Str "These are losses from the underfloor heating system itself downwards or sideways into unheated areas."], BulletList [[Plain [Strong [Str "Location:"], Str " The construction details show a floor assembly with insulation (XPS). However, if the insulation is not continuous, is under-dimensioned, or if there are thermal bridges (e.g., at the edges), heat from the underfloor loops will be lost downward."]], [Plain [Strong [Str "Impact:"], Str " This is heat that is \"emitted\" by the system but does not contribute to heating the intended space because it leaks into the ground or another non-habitable zone below."]], [Plain [Str "The calculated U-value for the floor separating the ground floor from the sanitary crawl space (", Code ("", [], []) "F2.1", Str ") is ", Strong [Str "0.19 W/m²K"], Str ". This means heat is constantly flowing from the heated floor into the crawl space, which is a direct emission loss."]]], Header 4 ("regulation-and-control-losses-pérdidas-por-regulación", ["unnumbered", "unlisted"], []) [Str "Regulation and Control Losses (Pérdidas por regulación)"], Para [Str "No control system is perfect. Inefficiencies arise from:"], BulletList [[Plain [Strong [Str "Overshooting:"], Str " The system heats slightly more than necessary."]], [Plain [Strong [Str "Hysteresis:"], Str " The system turns on/off around the setpoint, leading to an average temperature slightly different from the theoretical one."]], [Plain [Strong [Str "Inertia Mismatch:"], Str " The slow response time of underfloor heating can lead to periods where heat is being emitted even after the demand has been met."]]], Header 4 ("summary-the-system-efficiency-vs-boiler-efficiency", ["unnumbered", "unlisted"], []) [Str "Summary: The \"System Efficiency\" vs. \"Boiler Efficiency\""], Para [Str "The overall process from fuel to room heat looks like this, with losses at every stage:"], CodeBlock ("", [""], []) "┌─────────────────────────────────────────┐

│      Fuel Energy (100%)                 │

└─────────────────────────────────────────┘

               │

               ↓ [Boiler Losses ~7%]

               │

┌─────────────────────────────────────────┐

│  Useful Heat from Boiler                │

│  (93% - Nominal Efficiency)             │

└─────────────────────────────────────────┘

               │

               ↓ [Distribution Losses ~X%]

               │

┌─────────────────────────────────────────┐

│  Heat Reaching Underfloor Loops         │

└─────────────────────────────────────────┘

               │

               ↓ [Emission Losses ~Y%]

               │

┌─────────────────────────────────────────┐

│  Useful Heat Entering Room              │

│  (~75% - System Efficiency)             │

└─────────────────────────────────────────┘

", CodeBlock ("", ["mermaid"], []) "flowchart TD

    A[\"Fuel Energy<br/>100 percent\"] -->|\"Boiler Losses<br/>~7 percent\"| B[\"Useful Heat from Boiler<br/>93 percent - Nominal Efficiency\"]

    B -->|\"Distribution Losses<br/>~X percent\"| C[\"Heat Reaching<br/>Underfloor Loops\"]

    C -->|\"Emission Losses<br/>~Y percent\"| D[\"Useful Heat Entering Room<br/>~75 percent - System Efficiency\"]


    style A fill:#e3f2fd,stroke:#1976d2,stroke-width:2px

    style B fill:#fff3e0,stroke:#f57c00,stroke-width:2px

    style C fill:#fce4ec,stroke:#c2185b,stroke-width:2px

    style D fill:#e8f5e9,stroke:#388e3c,stroke-width:2px

", CodeBlock ("", ["plantuml"], []) "@startuml

skinparam component {

  BackgroundColor<<fuel>> LightBlue

  BackgroundColor<<boiler>> LightYellow

  BackgroundColor<<underfloor>> LightPink

  BackgroundColor<<room>> LightGreen

  BorderColor Black

  FontSize 11

}

skinparam ArrowFontSize 10

skinparam shadowing false


component \"Fuel Energy\\n**100%**\" <<fuel>> as fuel

component \"Useful Heat from Boiler\\n**93%** (Nominal Efficiency)\" <<boiler>> as boiler

component \"Heat Reaching\\nUnderfloor Loops\" <<underfloor>> as underfloor

component \"Useful Heat Entering Room\\n**~75%** (System Efficiency)\" <<room>> as room


fuel -down-> boiler : Boiler Losses\\n~7%

boiler -down-> underfloor : Distribution Losses\\n~X%

underfloor -down-> room : Emission Losses\\n~Y%

@enduml

", Para [Strong [Str "Conclusion:"]], Para [Str "HULC calculation of an effective ", Strong [Str "0.75 system efficiency"], Str " is realistic and correct from an overall energy balance perspective. It accounts for the ", Strong [Str "sum"], Str " of:"], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Strong [Str "Boiler Losses"], Str " (Nominal 7%)"]], [Plain [Strong [Str "Distribution Losses"], Str " (Pipes in crawl space)"]], [Plain [Strong [Str "Emission Losses"], Str " (Through the floor into the crawl space)"]], [Plain [Strong [Str "Regulation Losses"]]]], HorizontalRule, Header 2 ("primary-energy-consumption-for-heating", ["unnumbered", "unlisted"], []) [Str "Primary Energy Consumption for Heating"], Para [Str "This calculation converts the final energy consumption into primary energy (the energy from the source, considering extraction, processing, and transport) using official conversion factors."], Para [Strong [Str "Formulas:"]], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Code ("", [], []) "Primary Energy Total (kWh/m²·year) = Final Energy Consumption (kWh/m²·year) × f_ep,tot"]], [Plain [Code ("", [], []) "Primary Energy Non-Renewable (kWh/m²·year) = Final Energy Consumption (kWh/m²·year) × f_ep,non-ren"]], [Plain [Code ("", [], []) "Primary Energy Renewable (kWh/m²·year) = Final Energy Consumption (kWh/m²·year) × f_ep,ren"]]], Para [Strong [Str "Calculation for Option 2, Configuration 1:"]], BulletList [[Plain [Str "Final Energy Consumption = ", Code ("", [], []) "42.17 kWh/m²·year"]], [Plain [Str "Conversion Factors for Densified Biomass (Pellets):"], BulletList [[Plain [Code ("", [], []) "f_ep,tot", Str " (Total) = ", Code ("", [], []) "1.113"]], [Plain [Code ("", [], []) "f_ep,non-ren", Str " (Non-Renewable) = ", Code ("", [], []) "0.085"]], [Plain [Code ("", [], []) "f_ep,ren", Str " (Renewable) = ", Code ("", [], []) "1.028"]]]], [Plain [Strong [Str "Primary Energy Total ="], Str " ", Code ("", [], []) "42.17 × 1.113 = 46.94 kWh/m²·year"]], [Plain [Strong [Str "Primary Energy Non-Renewable ="], Str " ", Code ("", [], []) "42.17 × 0.085 = 3.58 kWh/m²·year"]], [Plain [Strong [Str "Primary Energy Renewable ="], Str " ", Code ("", [], []) "42.17 × 1.028 = 43.35 kWh/m²·year"]]], HorizontalRule, Header 2 ("heat-loss-calculation-for-acs-accumulator-relevant-for-the-mixed-system", ["unnumbered", "unlisted"], []) [Str "Heat Loss Calculation for ACS Accumulator (Relevant for the mixed system)"], Para [Str "Although this formula is in the ACS (Domestic Hot Water) section, it is highly relevant as the heating boiler also produces hot water. The formula calculates the heat losses from the storage tank."], Para [Strong [Str "Formula:"], SoftBreak, Code ("", [], []) "Q = A · U · DeltaT · Number of hours in the period"], Para [Strong [Str "Where:"]], BulletList [[Plain [Code ("", [], []) "Q", Str ": Heat losses produced in the accumulator during the period (Wh)"]], [Plain [Code ("", [], []) "A", Str ": Surface area of the accumulator's envelope (m²)"]], [Plain [Code ("", [], []) "U", Str ": Thermal transmittance of the accumulator's envelope (W/m²·K)"]], [Plain [Code ("", [], []) "DeltaT", Str ": Temperature difference between the inside of the tank and the ambient temperature outside it (°C)"]]], Para [Strong [Str "Simplified Application:"], SoftBreak, Code ("", [], []) "A · U", Str " can be simplified into a single \"loss coefficient\" for the tank."], BulletList [[Plain [Str "For a 100-liter tank (Options 1 & 2): Loss coefficient ", Code ("", [], []) "A·U = 0.5 W/°C"]], [Plain [Str "Assumed ", Code ("", [], []) "DeltaT", Str ": ", Code ("", [], []) "65°C (internal) - 20°C (ambient) = 45°C"]], [Plain [Strong [Str "Daily average loss for January (744 hours):"], Str " ", Code ("", [], []) "Q_daily = (0.5 W/°C × 45°C × 744 h) / 31 days = 540 Wh/day"]]], HorizontalRule, Header 2 ("summary-of-key-heating-system-data", ["unnumbered", "unlisted"], []) [Str "Summary of Key Heating System Data:"], BulletList [[Plain [Strong [Str "Production:"], Str " Individual biomass boiler."]], [Plain [Strong [Str "Thermal Power:"], Str " 25 kW."]], [Plain [Strong [Str "Fuel:"], Str " Biomass Pellets."]], [Plain [Strong [Str "Nominal Efficiency:"], Str " 93%."]], [Plain [Strong [Str "Distribution:"], Str " Water circuit with a supply temperature of 45°C."]], [Plain [Strong [Str "Emitters:"], Str " Underfloor heating."], BulletList [[Plain [Str "Ground Floor: ", Code ("", [], []) "70 W/m²"]], [Plain [Str "Attic Floor: ", Code ("", [], []) "85 W/m²"]]]]]]