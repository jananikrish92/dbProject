import psycopg2 as py
try:
	conn = py.connect("dbname = 'nobel_l' user = 'postgres' host = 'localhost' port='5433' password = 'db123'")
except:
	print "I cannot connect to db"
cur = conn.cursor()
cur.execute("""select pg_catalog.obj_description('name_1900'::regclass,'pg_class');""")
row1 = cur.fetchall()

cur.execute("""select pg_catalog.obj_description('name_1910'::regclass,'pg_class');""")
row2 = cur.fetchall()
print row1,"\n",row2


cur.execute("""select column_name from information_schema.columns where table_name='name_1900';""")
attrlist =cur.fetchall()

cur.execute("""select column_name from information_schema.columns where table_name='name_1910';""")
attrlist2 =cur.fetchall()

if set(attrlist2)==set(attrlist):
	flag ="true";


print flag
