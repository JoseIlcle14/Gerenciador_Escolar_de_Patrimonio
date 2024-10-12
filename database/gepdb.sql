

create table camera(
id int not null auto_increment,
consumo int not null,
marca varchar(20) not null,
idsala int not null,
primary key(id),
foreign key (idsala) references sala(id)
);

select * from sala;
select * from cadeiras;
select * from mesas;
select * from ar;
select * from ventilador;
select * from datashow;
select * from lousa;

DELETE FROM ventilador WHERE id = 31701;

select * from datashow;
update ar
set consumo = 300
where id =32501;
