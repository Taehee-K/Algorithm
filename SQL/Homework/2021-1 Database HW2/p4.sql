select Ships.name as name, Classes.displacement as weight
from Ships, Classes
where Ships.class = Classes.class and Classes.displacement > 35000
order by displacement, Ships.name;

select Ships.class
from Ships 
group by class
having count(class)=1;

select distinct Ships.name
from Ships
where Ships.class = 'Renown' or Ships.launched < 1919 or Ships.name in(
	select ship
	from Outcomes
	where battle = 'North Atlantic');

select Ships.name
from Ships, Classes
where Ships.class = Classes.class 
order by Classes.displacement, Ships.name;

select Outcomes.ship, 
date_format(Battles.beginDate, '%m-%Y') as beginDate, 
date_format(Battles.endDate,'%m-%Y') as endDate
from Outcomes, Battles
where Outcomes.battle = Battles.name and Battles.beginDate >= '1942-01-01' and Battles.endDate <= '1943-12-31';
