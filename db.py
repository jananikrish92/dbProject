import psycopg2 as py
import cosine
try:
	conn = py.connect("dbname = 'nobel_l' user = 'postgres' host = 'localhost' port='5433' password = 'db123'")
except:
	print "I cannot connect to db"
cur = conn.cursor()

cosineScoreList = []
plotTabList = []
cur.execute("""select distinct(table_name) from temp;""")
tabList = cur.fetchall()
print tabList
for i in range(len(tabList)):
	cur.execute("""select pg_catalog.obj_description(\'"""+str(tabList[i][0])+"""\'::regclass,'pg_class');""")
	row1 = cur.fetchall()
	cur.execute("""select column_name from information_schema.columns where table_name=\'"""+str(tabList[i][0])+"""\';""")
	attrlist =cur.fetchall()
	print row1
	tempTabList = []
	for j in range(i+1,len(tabList)):
		cur.execute("""select pg_catalog.obj_description(\'"""+str(tabList[j][0])+"""\'::regclass,'pg_class');""")
		row2 = cur.fetchall()
		a = str(row1[0][0])
		b = str(row2[0][0])
		vector1 = cosine.text_to_vector(a)
		vector2 = cosine.text_to_vector(b)
		cosine1 = cosine.get_cosine(vector1, vector2)
		cur.execute("""select column_name from information_schema.columns where table_name=\'"""+str(tabList[j][0])+"""\';""")
		attrlist2 = cur.fetchall()
		randScore = len(set(attrlist).intersection(attrlist2))/(len(attrlist)**2 + len(attrlist2)**2)**0.5
		cosineScoreList.append(cosine1+randScore)
		tempTabList.append(tabList[j][0])
	plotTabList.append([tabList[i][0],tempTabList])
print plotTabList 
# cur.execute("""select pg_catalog.obj_description('name_1900'::regclass,'pg_class');""")
# row1 = cur.fetchall()

# cur.execute("""select pg_catalog.obj_description('name_1910'::regclass,'pg_class');""")
# row2 = cur.fetchall()

# cur.execute("""select pg_catalog.obj_description('t1'::regclass,'pg_class');""")
# row3 = cur.fetchall()

# cur.execute("""select pg_catalog.obj_description('t2'::regclass,'pg_class');""")
# row4 = cur.fetchall()

# cur.execute("""select pg_catalog.obj_description('t3'::regclass,'pg_class');""")
# row5 = cur.fetchall()

# print row1[0][0],"\n",row2[0][0]

# a = str(row1[0][0])
# b = str(row2[0][0])
# c = str(row3[0][0])
# d = str(row4[0][0])
# e = str(row5[0][0])

# vector1 = cosine.text_to_vector(a)
# vector2 = cosine.text_to_vector(b)
# vector3 = cosine.text_to_vector(c)
# vector4 = cosine.text_to_vector(d)
# vector5 = cosine.text_to_vector(e)

# cosine1 = cosine.get_cosine(vector1, vector2)
# cosine2 = cosine.get_cosine(vector1, vector3)
# cosine3 = cosine.get_cosine(vector1, vector4)
# cosine4 = cosine.get_cosine(vector1, vector5)
# print 'Cosine:', cosine1,' ',cosine2,' ',cosine3,' ',cosine4

# if cosine > 0.5:
# 	cur.execute("""select column_name from information_schema.columns where table_name='name_1900';""")
# 	attrlist =cur.fetchall()

# 	cur.execute("""select column_name from information_schema.columns where table_name='name_1910';""")
# 	attrlist2 =cur.fetchall()

# 	cur.execute("""select column_name from information_schema.columns where table_name='t1';""")
# 	attrlist3 =cur.fetchall()

# 	cur.execute("""select column_name from information_schema.columns where table_name='t2';""")
# 	attrlist4 =cur.fetchall()

# 	cur.execute("""select column_name from information_schema.columns where table_name='t3';""")
# 	attrlist5 =cur.fetchall()

# 	if set(attrlist2)==set(attrlist):
# 		flag ="true";

# 	print len(set(attrlist).intersection(attrlist2))/(len(attrlist)**2 + len(attrlist2)**2)**0.5
# 	print len(set(attrlist).intersection(attrlist3))/(len(attrlist)**2 + len(attrlist3)**2)**0.5
# 	print len(set(attrlist).intersection(attrlist4))/(len(attrlist)**2 + len(attrlist4)**2)**0.5
# 	print len(set(attrlist).intersection(attrlist5))/(len(attrlist)**2 + len(attrlist5)**2)**0.5
	


# 	print flag
