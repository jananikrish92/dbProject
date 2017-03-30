create database nobel_l;
--Now run dbproj.py
select * from nobel limit 1;
--Create table to store laureates from 1900-1909
create table name_1900(id INTEGER, name TEXT,category TEXT,year TEXT);
--insert values
insert into name_1900(id,name,category,year)(select index,fullname,category,year from nobel where year>=1900 and year<=1909);
--Create table to store laureates from 1910-1919
create table name_1910(id INTEGER, name TEXT,category TEXT,year TEXT);
--insert values
insert into name_1910(id,name,category,year)(select index,fullname,category,year from nobel where year>=1910 and year<=1919);



create table t1(id integer,name text,category text,year text);
insert into t1( select index,full_name,category,year from nobel);


create table t2(id integer,prize text,motivation text,
	prize_share text,laureate_id integer, laureate_type text,full_name text,birth_date text,
 birth_city text,birth_country text,sex text,organization_name text,organization_city text,organization_country text,
death_date text, death_city text,death_country text);

insert into t2(select index,prize ,motivation ,prize_share ,laureate_id , laureate_type ,full_name ,birth_date ,
 birth_city ,birth_country ,sex ,organization_name ,organization_city ,organization_country ,
death_date , death_city ,death_country from nobel)
