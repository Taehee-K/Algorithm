select * from Classes;
select * from Ships;
insert into Classes values ('Nelson', 'bc', 'Gt. Britain', 8, 16, 34000);
insert into Ships values('Nelson', 'Nelson', 1927);
insert into Ships values('Rodney', 'Nelson', 1927);
select * from Classes;
select * from Ships;

select * from Classes;
select * from Ships;
insert into Classes values ('Vittorio Veneto', 'bb', 'Italy', 9, 15, 41000);
insert into Ships values('Vittorio Veneto', 'Vittorio Veneto', 1940);
insert into Ships values('Italia', 'Vittorio Veneto', 1940);
insert into Ships values('Roma', 'Vittorio Veneto', 1942);
select * from Classes;
select * from Ships;

select * from Ships;
select * from Outcomes;
delete from Ships
where name in (
	select ship
	from Outcomes	
	where battle = 'Surigao Strait' and result = 'sunk'
);
select * from Ships;
select * from Outcomes;

select * from Classes;
update Classes
set bore  = bore * 2.5, displacement = displacement/1.1;
select * from Classes;

select * from Outcomes;
update Outcomes
set result = 'damaged'
where ship in (
	select name
	from Ships as S, Classes as C
	where S.class = C.class and C.numGuns = 8
);
select * from Outcomes;

select * from Battles;
update Battles
set beginDate = '1941-04-24'
where name = 'North Atlantic';
select * from Battles;

select * from Ships;
select * from Classes;	
delete from Classes
where class in(
	select class
	from (
		select class
		from Classes as C natural left outer join Ships as S
		group by C.class
		having count(S.name) < 3) as temp
);
select * from Ships;
select * from Classes;	