select abs(annual_heating_kwh_m2) + annual_cooling_kwh_m2 as total_energy_demmand_kwh_m2,
       (abs(annual_heating_kwh_m2) + annual_cooling_kwh_m2)*64 as total_energy_demmand_kwh
from results_building_summary bld
where project_name='EjemploI_2526_Option1_Config1';