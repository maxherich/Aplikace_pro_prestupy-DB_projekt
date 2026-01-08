create table klub(
	id int primary key auto_increment,
    nazev varchar(30) not null,
    liga_id int not null,
    foreign key (liga_id) references liga(id),
    majitel_id int not null,
    foreign key(majitel_id) references majitel(id)
);

create table hrac(
	id int primary key auto_increment,
    jmeno varchar(30) not null,
    prijmeni varchar(30) not null,
    cislo_dresu int check(cislo_dresu > 0 and cislo_dresu < 100) not null,
    pozice enum('brankar', 'obrance', 'zaloznik', 'utocnik') not null,
    klub_id int not null,
    foreign key (klub_id) references klub(id)
);

create table prestup(
	id int primary key auto_increment,
    hrac_id int not null,
    foreign key(hrac_id) references hrac(id),
    prodavajici_klub_id int not null,
    foreign key(prodavajici_klub_id) references klub(id),
    kupujici_klub_id int not null,
    foreign key(prodavajici_klub_id) references klub(id),
    datum date not null,
    cena float not null,
    check(prodavajici_klub_id != kupujici_klub_id)
);

create table majitel(
	id int primary key auto_increment,
    jmeno varchar(30) not null,
    prijmeni varchar(30) not null,
    email varchar(30) not null,
    rozpocet float not null check (rozpocet > 0),
    aktivni bool not null
);

create table liga(
	id int primary key auto_increment,
    nazev varchar(30) not null,
    zeme varchar(30) not null,
    uroven enum('1. liga', '2. liga', '3.liga') not null
);

LOAD DATA LOCAL INFILE 'D:\max\SKOLA\PV\PV-DB-projekt_fotbalovy_trh\csv_data\hrac.csv' INTO TABLE hrac FIELDS TERMINATED BY ',' IGNORE 1 ROWS;
SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;

insert into prestup(hrac_id, prodavajici_klub_id, kupujici_klub_id, datum, cena) values (1, 1, 2, sysdate(), 100000);

delimiter //
create trigger dokonceni_nakupu_hrace
after insert
on prestup
for each row
begin	
	call nakup_hrace(new.kupujici_klub_id, new.prodavajici_klub_id, new.hrac_id);
end//
delimiter ;

delimiter //
create procedure nakup_hrace (kupujici_klub_id int, prodavajici_klub_id int, hrac_id int)
begin	
	start transaction;
    update hrac set klub_id = kupujici_klub_id where id = new.hrac_id;
    update majitel set rozpocet = rozpocet - cena where id = (select majitel_id from klub where id = kupujici_klub_id);
    update majitel set rozpocet = rozpocet + cena where id = (select majitel_id from klub where id = prodavajici_klub_id);
    commit;
end//
delimiter ;

