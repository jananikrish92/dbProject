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
