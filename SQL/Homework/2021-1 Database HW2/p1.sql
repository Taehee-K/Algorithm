create table Classes(
	class varchar(25),
	type varchar(5),
	country varchar(20),
	numGuns int,
	bore int,
	displacement int,
	primary key(class)
);
describe Classes;

create table Ships(
	name varchar(25),
	class varchar(25),
	launched int(4),
	primary key(name),
	foreign key(class) references Classes(class)
);
describe Ships;

create table Battles(
	name varchar(25),
	beginDate date,
	endDate date,
	primary key(name)
);
describe Battles;

create table Outcomes(
	ship varchar(25),
	battle varchar (25),
	result varchar(10),
	primary key(ship, battle),
	foreign key(ship) references Ships(name),
	foreign key(battle) references Battles(name)
);
describe Outcomes;
