
create table academy_award(name TEXT,film TEXT,award TEXT,year TEXT);
insert into academy_award(select name,film,award,year from academy);

create table actor_film(name TEXT,film TEXT);
insert into actor_film(select name,film from academy);

create table film_award_2000(film TEXT,award TEXT,year TEXT);
insert into film_award_2000(select film,award,year from academy where year like '2%');

create table film_award_1950(film TEXT,award TEXT,year TEXT);
insert into film_award_1950(select film,award,year from academy where year like '195%' or year like '196%' or year like '197%' or year like '198%' or year like '199%');

create table film_award_1927(film TEXT,award TEXT,year TEXT);
insert into film_award_1927(select film,award,year from academy where year like '192%' or year like '193%' or year like '194%');
