select class, country 
from Classes
where numGuns>=10;

select class, numGuns, bore
from Classes
where numGuns!=9 and bore<16
order by displacement, bore, numGuns;

select country
from Classes
where type = 'bc';

select name as newship
from Ships 
where launched > 1918;

select name 
from Ships
where name like '% % %';