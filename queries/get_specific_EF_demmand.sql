select * from ef_monthly_components efmc,ep_meta m
where efmc.project_id=m.id
  and m.project_name like "EjemploI_2526_%"
and efmc.month_name='Ene';


select id,
       project_id,
       carrier,
       ctype,
       csubtype,
       service,
       annual_value,
       comment
from ef_annual_components efac where efac.project_id = 1;

SELECT
    m.project_name,
       efac.carrier,
       efac.ctype,
       efac.csubtype,
       efac.service,
       round(efac.annual_value/m.arearef,2) as "specific consumption Ep annual value",
       efac.comment
FROM ef_annual_components efac,ep_meta m
where efac.project_id=m.id
and m.project_name like "EjemploI_2526_%"
;

-- Final Energy consumption by Carrier and Service
SELECT m.project_name,
       efac.carrier,
       efac.service,
       round(sum(efac.annual_value),2)           as "consumption Final Energy annual value (kWh/year)",
       round(sum(efac.annual_value)/m.arearef,2) as "specific consumption Final Energy annual value (kWh/m^2*year)"
FROM ef_annual_components efac,ep_meta m
where efac.project_id=m.id
and m.project_name like "EjemploI_2526_%"
group by m.project_name,
         efac.carrier,
    efac.service
;

-- Final Energy consumption by Carrier
SELECT m.project_name,
       efac.carrier,
       round(sum(efac.annual_value),2) as "consumption Final Energy annual value (kWh/year)",
       round(sum(efac.annual_value)/m.arearef,2) as "specific consumption Final Energy annual value (kWh/m^2*year)"
FROM ef_annual_components efac,ep_meta m
where efac.project_id=m.id
  and m.project_name like "EjemploI_2526_%"
group by m.project_name,
         efac.carrier
;

--------------------------------------------------------------------
-- building loads
SELECT
    concept,
    heating_net_kwh_m2,
    cooling_net_kwh_m2
FROM
    results_zone_by_concept
WHERE
    project_name = 'EjemploI_2526_Option1_Config1';