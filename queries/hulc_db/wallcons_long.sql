select * from wallcons_long where name='MURO EXTERIOR';

select name, sum(wallcons_long.thickness) from wallcons_long where name='MURO EXTERIOR'
group by name ;;