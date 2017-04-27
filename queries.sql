
--Now run dbproj.py
select * from nobel limit 1;

create table name_1900_1909(name TEXT,category TEXT,year TEXT);
insert into name_1900_1909(name,category,year)(select full_name,category,year from nobel where year>=1900 and year<=1909);

create table name_1910_1919(name TEXT,category TEXT,year TEXT);
insert into name_1910_1919(name,category,year)(select full_name,category,year from nobel where year>=1910 and year<=1919);

create table name_1920_1929(name TEXT,category TEXT,year TEXT);
insert into name_1920_1929(name,category,year)(select full_name,category,year from nobel where year>=1920 and year<=1929);

create table name_1930_1939(name TEXT,category TEXT,year TEXT);
insert into name_1930_1939(name,category,year)(select full_name,category,year from nobel where year>=1930 and year<=1939);

create table name_1940_1949(name TEXT,category TEXT,year TEXT);
insert into name_1940_1949(name,category,year)(select full_name,category,year from nobel where year>=1940 and year<=1949);

create table name_1950_1959(name TEXT,category TEXT,year TEXT);
insert into name_1950_1959(name,category,year)(select full_name,category,year from nobel where year>=1950 and year<=1959);

create table name_1960_1969(name TEXT,category TEXT,year TEXT);
insert into name_1960_1969(name,category,year)(select full_name,category,year from nobel where year>=1960 and year<=1969);


create table nobel_prize(name TEXT,prize TEXT);
insert into nobel_prize(select full_name,prize from nobel);

create table nobel_lauretes_country(name TEXT, birth_country TEXT, category TEXT);
insert into nobel_lauretes_country(select full_name,birth_country,category from nobel);

create table nobel_lauretes_city(name TEXT,birth_city TEXT,year TEXT, category TEXT);
insert into nobel_lauretes_city(select full_name,birth_city,year,category from nobel);

create table nobel_lauretes_data(id integer,prize text,motivation text,
	prize_share text,laureate_id integer, laureate_type text,full_name text,birth_date text,
 birth_city text,birth_country text,sex text,organization_name text,organization_city text,organization_country text,
death_date text, death_city text,death_country text);

 
insert into nobel_lauretes_data(select index,prize ,motivation ,prize_share ,laureate_id , laureate_type ,full_name ,birth_date ,
 birth_city ,birth_country ,sex ,organization_name ,organization_city ,organization_country ,
death_date , death_city ,death_country from nobel);
