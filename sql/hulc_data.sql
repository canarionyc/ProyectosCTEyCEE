select * from wallcons;

-- Muro exterior

select * from wallcons_long where name='MURO EXTERIOR';

select name, sum(wallcons_long.thickness) from wallcons_long where name='MURO EXTERIOR'
group by name ;

select * from materials where  name='Teja de arcilla cocida';

select wc.name
     , wc.material
     , round(wc.thickness,3) as thickness
     , round(m.conductivity,3) as conductivity
     , round(m.resistance,3) as resistance
     , m.density
,m.*
from wallcons_long wc, materials m  where wc.name='MURO EXTERIOR' and wc.material=m.name;

select wc.name
     , round(sum(wc.thickness),3) as thickness
     , round(sum(wc.thickness* m.density),3) as mass
     , round(sum(case when m.conductivity>0 then wc.thickness/m.conductivity else m.resistance end),3) as resitance
from wallcons_long wc, materials m  where wc.name='MURO EXTERIOR' and wc.material=m.name;

-- Cubierta

select * from wallcons_long where name='CUB IN TEJA';

select wc.name
     , count(1) as num_capas
     , round(sum(wc.thickness),3) as thickness
     , round(sum(wc.thickness* m.density),3) as mass
     , round(sum(case when m.conductivity>0 then wc.thickness/m.conductivity else m.resistance end),3) as resitance
from wallcons_long wc, materials m  where wc.name='CUB IN TEJA' and wc.material=m.name;

-- suelo
select * from wallcons_long where name='FOR CAM SANIT';

select wc.name
     , count(1) as num_capas
     , round(sum(wc.thickness),3) as thickness
     , round(sum(wc.thickness* m.density),3) as mass
     , round(sum(case when m.conductivity>0 then wc.thickness/m.conductivity else m.resistance end),3) as resitance
from wallcons_long wc, materials m  where wc.name='FOR CAM SANIT' and wc.material=m.name;
