select country
from Classes
where numGuns in(
	select max(numGuns)
	from Classes
);

select country 
from Classes
where numGuns >= all(
	select numGuns
	from Classes
);

select class 
from Ships
where name in(
	select ship 
	from Outcomes
	where result = 'damaged'
);

select class
from Ships 
where exists(
	select ship 
	from Outcomes
	where result = 'damaged' and Ships.name = Outcomes.ship
);

select name 
from Ships
where class in(
	select class 
	from Classes
	where bore = 16
);

select name
from Ships 
where exists(
	select class
	from Classes
	where bore = 16 and Ships.class = Classes.class
);

select battle 
from Outcomes
where ship in(
	select name
	from Ships
	where class = 'Kongo'
);

select battle 
from Outcomes 
where exists(
	select name
	from Ships
	where class = 'Kongo' and Outcomes.ship = Ships.name
);

select S.name
from Ships as S, Classes as C
where S.class = C.class and numGuns in (
	select max(numGuns)
	from Ships as S2, Classes as C2	
	where S2.class = C2.class and C.bore = C2.bore
);

select S.name	
from Ships as S, Classes as C
where S.class = C.class and numGuns >= all(
	select numGuns
	from Ships as S2, Classes as C2
	where S2.class = C2.class and C.bore = C2.bore
);