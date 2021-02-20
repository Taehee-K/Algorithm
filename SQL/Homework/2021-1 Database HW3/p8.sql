alter table Classes drop bore;
describe Classes;
select * from Classes;

alter table Ships 
add company varchar(15) default 'ShipCompany';
describe Ships;
select * from Ships;
