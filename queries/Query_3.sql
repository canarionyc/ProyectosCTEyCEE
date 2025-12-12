select value from metadata where key='CTE_AREAREF';

select c.*, vm.* from consumos c, valores_mensuales vm where vm.entry_id=c.id;

select c.servicio,
       round(sum(vm.valor)/(select value from metadata where key='CTE_AREAREF'),2) as 'kWh/m2'
from consumos c, valores_mensuales vm
where vm.entry_id=c.id
group by c.servicio;