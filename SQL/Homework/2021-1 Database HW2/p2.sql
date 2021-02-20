insert into Classes values ('Bismarck', 'bb', 'Germany', 8, 15, 42000);
insert into Classes values ('Iowa', 'bb', 'USA', 9, 16, 46000);
insert into Classes values ('Kongo', 'bc', 'Japan', 8, 14, 32000);
insert into Classes values ('North Carolina', 'bb', 'USA', 9, 16, 37000);
insert into Classes values ('Renown', 'bc', 'Gt. Britain', 6, 15, 32000);
insert into Classes values ('Revenge', 'bb', 'Gt. Britain', 8, 15, 29000);
insert into Classes values ('Tennessee', 'bb', 'USA', 12, 14, 32000);
insert into Classes values ('Yamato', 'bb', 'Japan', 9, 18, 65000);

insert into Battles values('North Atlantic','1941-05-24', '1941-05-27' );
insert into Battles values('Guadalcanal','1942-11-15', '1942-11-15' );
insert into Battles values('North Cape','1943-12-26', '1943-12-26' );
insert into Battles values('Surigao Strait','1944-10-25', '1944-10-25' );

insert into Ships values('Prince of Wales', 'Tennessee', 1921);
insert into Ships values('Bismarck', 'Bismarck', 1915);
insert into Ships values('Duke of York', 'Kongo', 1914);
insert into Ships values('Iowa', 'Iowa', 1943);
insert into Ships values('Kirishima', 'Kongo', 1915);
insert into Ships values('Kongo', 'Kongo', 1913);
insert into Ships values('Fuso', 'Iowa', 1943);
insert into Ships values('Yamashiro', 'Yamato', 1942);
insert into Ships values('California', 'Iowa', 1943);
insert into Ships values('North Carolina', 'North Carolina', 1941);
insert into Ships values('Renown', 'Renown', 1916);
insert into Ships values('Hood', 'Renown', 1916);
insert into Ships values('Scharnhorst', 'Revenge', 1916);
insert into Ships values('Revenge', 'Revenge', 1916);
insert into Ships values('King George V', 'Revenge', 1916);
insert into Ships values('South Dakota', 'Revenge', 1916);
insert into Ships values('Tennessee', 'Tennessee', 1920);
insert into Ships values('Washington', 'North Carolina', 1941);
insert into Ships values('West Virginia', 'Iowa', 1943);
insert into Ships values('Yamato', 'Yamato', 1941);

insert into Outcomes values('Bismarck', 'North Atlantic', 'sunk');
insert into Outcomes values('California', 'Surigao Strait', 'ok');
insert into Outcomes values('Duke of York', 'North Cape', 'ok');
insert into Outcomes values('Duke of York', 'Surigao Strait', 'ok');
insert into Outcomes values('Fuso', 'Surigao Strait', 'sunk');
insert into Outcomes values('Hood', 'North Atlantic', 'sunk');
insert into Outcomes values('King George V', 'North Atlantic', 'ok');
insert into Outcomes values('Kirishima', 'Guadalcanal', 'sunk');
insert into Outcomes values('Prince of Wales', 'North Atlantic', 'damaged');
insert into Outcomes values('Prince of Wales', 'North Cape', 'ok');
insert into Outcomes values('Scharnhorst', 'North Cape', 'sunk');
insert into Outcomes values('South Dakota', 'Guadalcanal', 'damaged');
insert into Outcomes values('Tennessee', 'Surigao Strait', 'sunk');
insert into Outcomes values('Washington', 'Guadalcanal', 'ok');
insert into Outcomes values('West Virginia', 'Surigao Strait', 'ok');
insert into Outcomes values('Yamashiro', 'Surigao Strait', 'ok');


select * from Classes;
select * from Battles;
select * from Ships;
select * from Outcomes;
