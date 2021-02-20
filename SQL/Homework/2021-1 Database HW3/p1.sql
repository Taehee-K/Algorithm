create table Classes(
	class varchar(25),
	type varchar(5),
	country varchar(20),
	numGuns int,
	bore numeric(5, 1),
	displacement numeric(6, 1),
	primary key(class)
);
describe Classes;
show create table Classes;

create table Ships(
	name varchar(25),
	class varchar(25),
	launched int(4),
	primary key(name),
	foreign key(class) references Classes(class)
		on delete cascade
		on update cascade 
);
describe Ships;
show create table Ships;

create table Battles(
	name varchar(25),
	beginDate date,
	endDate date,
	primary key(name)
);
describe Battles;
show create table Battles;

create table Outcomes(
	ship varchar(25),
	battle varchar (25),
	result varchar(10),
	primary key(ship, battle),
	foreign key(ship) references Ships(name)
		on delete cascade
		on update cascade,
	foreign key(battle) references Battles(name)
		on delete cascade
		on update cascade
);
describe Outcomes;
show create table Outcomes;
