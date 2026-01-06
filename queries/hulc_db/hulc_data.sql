select * from wallcons;

select * from wallcons where name='MURO EXTERIOR0.60';

delete  from wallcons where name='MURO EXTERIOR0.60';
delete  from wallcons_long where name='MURO EXTERIOR0.60';
-- SOL CAM SANIT

select wc.name
     ,wc2.revit_category
     , wc.material
     , m.material_group
     , round(wc.thickness,4) as thickness
     , round(m.conductivity,4) as conductivity
     , round(m.resistance,4) as resistance
     , round(m.density,4) as density
     , round(m.specificheat,4) as specificheat
     , round(m.vapourdiffusivity,4) as vapourdiffusivity
from wallcons_long wc, materials m, wallcons wc2
where wc.material=m.name
  and wc.name=wc2.name
and wc.name in ('FOR CAM SANIT', 'SOL CAM SANIT', 'FOR INT AC-NH'
    );


select * from wallcons_long where name='SOL CAM SANIT';
-- MURO EXTERIOR

select * from wallcons_long where name='MURO EXTERIOR';

select name, sum(wallcons_long.thickness) from wallcons_long where name='MURO EXTERIOR'
group by name ;



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
select * from materials where  name='Teja de arcilla cocida';

select * from wallcons_long where name='CUB IN TEJA';

select wc.name
     , count(1) as num_capas
     , round(sum(wc.thickness),3) as thickness
     , round(sum(wc.thickness* m.density),3) as mass
     , round(sum(case when m.conductivity>0 then wc.thickness/m.conductivity else m.resistance end),3) as resitance
from wallcons_long wc, materials m  where wc.name='CUB IN TEJA' and wc.material=m.name;

-- floor detailed
select * from wallcons_long where name='FOR CAM SANIT';

-- floor aggregated
select wc.name
     , count(1) as num_capas
     , round(sum(wc.thickness),3) as thickness
     , round(sum(wc.thickness* m.density),3) as mass
     , round(sum(case when m.conductivity>0 then wc.thickness/m.conductivity else m.resistance end),3) as resitance
from wallcons_long wc, materials m  where wc.name='FOR CAM SANIT' and wc.material=m.name;

-- wincons
select * from wincons;