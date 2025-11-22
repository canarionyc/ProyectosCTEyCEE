setlocal
set PATH=c:\bin;%PATH%
del  Ejemplo_I_Config_2.pdf
@echo on

cd src
dir
dir floor_heating.mmd

rem call mmdc -i floor_heating.mmd -o floor_heating.png -w 2400 -b transparent
call mmdc -i floor_heating.mmd -o floor_heating.pdf -c mermaid-config.json


pandoc ^
  01_Ejemplo1_Config2_Thermal_Envelope.md ^
  Ejemplo1_Config2_Heating.md ^
  Ejemplo1_Config2_Water_Heating.md ^
  Ejemplo1_Config2_Cooling.md ^
  Ejemplo1_Config2_Ventilation.md ^
  Ejemplo1_Config2_Condensations.md ^
  Ejemplo1_Config2_Air_Tightness.md ^
  --from=markdown+lists_without_preceding_blankline ^
  -o ..\Ejemplo_I_Config_2.pdf ^
  --pdf-engine=xelatex ^
  --variable mainfont="DejaVu Sans" ^
  --variable monofont="DejaVu Sans Mono" ^
  --variable geometry:margin=1.5cm ^
  --variable documentclass=article ^
  --variable classoption=10pt ^
  --variable header-includes="\usepackage{graphicx}\usepackage{fvextra}\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\},samepage}" ^
  --wrap=none
endlocal
dir Ejemplo_I_Config_2.pdf

