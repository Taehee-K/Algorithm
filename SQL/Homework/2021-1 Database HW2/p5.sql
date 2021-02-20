select count(distinct class)
from Classes
where type = 'bb';

select avg(Classes.numGuns)
from Classes, Ships 
where Classes.class = Ships.class and type = 'bb';

select Classes.class, min(Ships.launched)
from Classes, Ships 
where Classes.class = Ships.class 
group by class;

select C.class, count(O.result) as sunk
from Classes as C, Ships as S, Outcomes as O
where C.class = S.class and S.name = O.ship and O.result = 'sunk' and S.class in (
	select class
	from Ships
	group by class
	having count(class)>=3)
group by C.class
having count(O.result)>0;

select O.battle, sum(numGuns) as totalGuns
from Classes as C, Ships as S, Outcomes as O
where C.class = S.class and S.name = O.ship 
group by O.battle;