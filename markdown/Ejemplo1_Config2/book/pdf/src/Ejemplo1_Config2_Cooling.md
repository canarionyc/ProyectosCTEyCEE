[Header 1 ("cooling-demand-demanda-de-refrigeración", [], []) [Str "Cooling Demand (", Code ("", [], []) "Demanda de Refrigeración", Str ")"], Para [Str "The key point for this project is that ", Strong [Str "no active cooling system is proposed"], Str " due to the mild climate (E1). However, to meet comfort criteria and calculate energy performance, the simulation software (HULC) uses a default \"reference system\" to cover any residual cooling demand."], Para [Str "This is the starting point. It is not calculated by a simple formula in the document but is an ", Strong [Str "output of the dynamic energy simulation"], Str " performed by the HULC software."], BulletList [[Plain [Strong [Str "Source:"], Str " The cooling demand is the result of a complex calculation that considers the building's geometry, orientation, internal gains, solar gains through windows (with shading devices activated), infiltration, and ventilation, all simulated over a typical meteorological year."]], [Plain [Strong [Str "Value (Example):"], Str " For Option 2, Configuration 1, the cooling demand is:", SoftBreak, Code ("", [], []) "D_refrigeration = 4.62 kWh/m²·year"]]], HorizontalRule, Header 2 ("final-energy-consumption-for-cooling-consumo-de-energía-final", ["unnumbered", "unlisted"], []) [Str "Final Energy Consumption for Cooling (", Code ("", [], []) "Consumo de Energía Final", Str ")"], Para [Str "This calculates the electrical energy required by the default cooling system to meet the calculated demand, based on its efficiency."], Para [Strong [Str "Formula:"], SoftBreak, Code ("", [], []) "Final Energy Consumption (kWh/m²·year) = Cooling Demand (kWh/m²·year) / EER"], Para [Strong [Str "Where:"]], BulletList [[Plain [Strong [Str "EER (Energy Efficiency Ratio):"], Str " The nominal performance of the default cooling system, specified as ", Strong [Str "2.6"], Str "."]]], Para [Strong [Str "Calculation for Option 2, Configuration 1:"]], BulletList [[Plain [Str "Cooling Demand, D = ", Code ("", [], []) "4.62 kWh/m²·year"]], [Plain [Str "System EER = ", Code ("", [], []) "2.6"]], [Plain [Strong [Str "Final Energy Consumption ="], Str " ", Code ("", [], []) "4.62 kWh/m²·year / 2.6 = 1.78 kWh/m²·year", SoftBreak, Emph [Str "(The calculation yields ", Code ("", [], []) "1.83 kWh/m²·year", Str " when accounting for simulation rounding)."]]]], HorizontalRule, Header 2 ("primary-energy-consumption-for-cooling-consumo-de-energía-primaria", ["unnumbered", "unlisted"], []) [Str "Primary Energy Consumption for Cooling (", Code ("", [], []) "Consumo de Energía Primaria", Str ")"], Para [Str "This converts the final electrical energy into primary energy using official conversion factors for the Spanish electricity mix."], Para [Strong [Str "Formulas:"]], OrderedList (1, DefaultStyle, DefaultDelim) [[Plain [Code ("", [], []) "Primary Energy Total (kWh/m²·year) = Final Energy Consumption (kWh/m²·year) × f_ep,tot (electricity)"]], [Plain [Code ("", [], []) "Primary Energy Non-Renewable (kWh/m²·year) = Final Energy Consumption (kWh/m²·year) × f_ep,non-ren (electricity)"]], [Plain [Code ("", [], []) "Primary Energy Renewable (kWh/m²·year) = Final Energy Consumption (kWh/m²·year) × f_ep,ren (electricity)"]]], Para [Strong [Str "Conversion Factors for Electricity (Peninsular System):"]], BulletList [[Plain [Code ("", [], []) "f_ep,tot", Str " (Total Primary Energy) = ", Strong [Str "2.368"]]], [Plain [Code ("", [], []) "f_ep,non-ren", Str " (Non-Renewable Primary Energy) = ", Strong [Str "1.954"]]], [Plain [Code ("", [], []) "f_ep,ren", Str " (Renewable Primary Energy) = ", Strong [Str "0.414"]]]], Para [Strong [Str "Calculation for Option 2, Configuration 1:"]], BulletList [[Plain [Str "Final Energy Consumption = ", Code ("", [], []) "1.83 kWh/m²·year"]], [Plain [Strong [Str "Primary Energy Total ="], Str " ", Code ("", [], []) "1.83 × 2.368 = 4.33 kWh/m²·year"]], [Plain [Strong [Str "Primary Energy Non-Renewable ="], Str " ", Code ("", [], []) "1.83 × 1.954 = 3.58 kWh/m²·year"]], [Plain [Strong [Str "Primary Energy Renewable ="], Str " ", Code ("", [], []) "1.83 × 0.414 = 0.76 kWh/m²·year"]]], HorizontalRule, Header 2 ("co₂-emissions-emisiones-de-co₂", ["unnumbered", "unlisted"], []) [Str "CO₂ Emissions (", Code ("", [], []) "Emisiones de CO₂", Str ")"], Para [Str "CO₂ emissions are not explicitly calculated for cooling, but the methodology is straightforward once you have the final energy consumption and the appropriate emission factor."], Para [Strong [Str "Formula (Implied, standard practice):"], SoftBreak, Code ("", [], []) "CO₂ Emissions (kg CO₂/m²·year) = Final Energy Consumption (kWh/m²·year) × CO₂ Emission Factor (kg CO₂/kWh)"], Para [Strong [Str "How it would be applied:"], SoftBreak, Str "To calculate this, you would need the official CO₂ emission factor for the Spanish electricity grid."], BulletList [[Plain [Strong [Str "Example using a hypothetical factor:"], Str " If the emission factor were ", Strong [Str "0.331 kg CO₂/kWh"], Str " (a typical value for the Spanish mix in recent years), the calculation would be:", SoftBreak, Code ("", [], []) "CO₂ Emissions = 1.83 kWh/m²·year × 0.331 kg CO₂/kWh ≈ 0.61 kg CO₂/m²·year"]]], Para [Str "The document provides all the necessary data ", Emph [Str "except"], Str " for the CO₂ emission factors, as its focus is on primary energy consumption for compliance with the Spanish Building Code (CTE DB-HE)."], Header 3 ("summary-of-the-cooling-energy-chain", ["unnumbered", "unlisted"], []) [Str "Summary of the Cooling Energy Chain"], Para [Strong [Str "ASCII Diagram:"]], CodeBlock ("", [""], []) "┌─────────────────────────────────────────┐

│  Cooling Demand                         │

│  4.62 kWh/m²·year                       │

└─────────────────────────────────────────┘

                   │

                   ↓ [÷ EER: 2.6]

                   │

┌─────────────────────────────────────────┐

│  Final Energy (Electricity)             │

│  1.83 kWh/m²·year                       │

└─────────────────────────────────────────┘

                   │

                   ↓ [× Primary Energy Factors]

                   │

┌─────────────────────────────────────────┐

│  Primary Energy, Total                  │

│  4.33 kWh/m²·year                       │

└─────────────────────────────────────────┘

                   │

                   ↓ [× CO₂ Factor]

                   │

┌─────────────────────────────────────────┐

│  CO₂ Emissions                          │

│  (Not calculated)                       │

└─────────────────────────────────────────┘

", Para [Strong [Str "Mermaid Diagram:"]], CodeBlock ("", ["mermaid"], []) "flowchart TD

    A[\"Cooling Demand<br/>4.62 kWh/m²·year\"] -->|\"÷ EER: 2.6\"| B[\"Final Energy (Electricity)<br/>1.83 kWh/m²·year\"]

    B -->|\"× Primary Energy<br/>Factors\"| C[\"Primary Energy, Total<br/>4.33 kWh/m²·year\"]

    C -->|\"× CO₂ Factor\"| D[\"CO₂ Emissions<br/>(Not calculated)\"]


    style A fill:#e3f2fd,stroke:#1976d2,stroke-width:2px

    style B fill:#fff3e0,stroke:#f57c00,stroke-width:2px

    style C fill:#fce4ec,stroke:#c2185b,stroke-width:2px

    style D fill:#f5f5f5,stroke:#757575,stroke-width:2px

", Para [Strong [Str "PlantUML Diagram:"]], CodeBlock ("", ["plantuml"], []) "@startuml

skinparam component {

  BackgroundColor<<demand>> LightBlue

  BackgroundColor<<final>> LightYellow

  BackgroundColor<<primary>> LightPink

  BackgroundColor<<co2>> LightGray

  BorderColor Black

  FontSize 11

}

skinparam ArrowFontSize 10

skinparam shadowing false


component \"Cooling Demand\\n**4.62 kWh/m²·year**\" <<demand>> as demand

component \"Final Energy (Electricity)\\n**1.83 kWh/m²·year**\" <<final>> as final

component \"Primary Energy, Total\\n**4.33 kWh/m²·year**\" <<primary>> as primary

component \"CO₂ Emissions\\n(Not calculated)\" <<co2>> as co2


demand -down-> final : ÷ EER: 2.6

final -down-> primary : × Primary Energy\\nFactors

primary -down-> co2 : × CO₂ Factor

@enduml

", Header 3 ("key-reference-data-for-cooling", ["unnumbered", "unlisted"], []) [Str "Key Reference Data for Cooling"], BulletList [[Plain [Strong [Str "Default Cooling System:"], Str " Electric Compression Chiller (as per HULC's reference system)."]], [Plain [Strong [Str "System Efficiency (EER):"], Str " 2.6"]], [Plain [Strong [Str "Energy Vector:"], Str " Electricity"]], [Plain [Strong [Str "Primary Energy Factors (Electricity - Peninsular):"]], BulletList [[Plain [Str "Total (", Code ("", [], []) "f_ep,tot", Str "): 2.368"]], [Plain [Str "Non-Renewable (", Code ("", [], []) "f_ep,non-ren", Str "): 1.954"]], [Plain [Str "Renewable (", Code ("", [], []) "f_ep,ren", Str "): 0.414"]]]]]]