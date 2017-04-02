import psycopg2 as py
import cosine
try:
	conn = py.connect("dbname = 'nobel_l' user = 'postgres' host = 'localhost' port='5433' password = 'db123'")
except:
	print "I cannot connect to db"
cur = conn.cursor()
cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public' and table_name not in ('nobel', 'temp', 'index_table');""")
tableList = cur.fetchall()
finalScoreList = [] 
for t in range(len(tableList)):
	cur.execute("""select column_name from information_schema.columns where table_name=\'"""+tableList[t][0]+"""\';""")
	col1 = cur.fetchall()	
	cur.execute("""select pg_catalog.obj_description(\'"""+str(tableList[t][0])+"""\'::regclass,'pg_class');""")
	row1 = cur.fetchall()
	a = str(row1[0][0])
	vector1 = cosine.text_to_vector(a)
	scoreList = []
	for t1 in range(len(tableList)):
		if t!=t1:
			cur.execute("""select column_name from information_schema.columns where table_name=\'"""+tableList[t1][0]+"""\';""")
			col2 = cur.fetchall()
			cur.execute("""select pg_catalog.obj_description(\'"""+str(tableList[t1][0])+"""\'::regclass,'pg_class');""")
			row2 = cur.fetchall()
			b = str(row2[0][0])
			vector2 = cosine.text_to_vector(b)
			cosine1 = cosine.get_cosine(vector1, vector2)
			score =0
			for i in range(len(col1)):
			    cur.execute("""select """+col1[i][0]+""" from """+tableList[t][0]+""";""")
			    list1 = cur.fetchall()
			    for j in range(len(col2)):
					cur.execute("""select """+col2[j][0]+""" from """+tableList[t1][0]+""";""")
					list2 = cur.fetchall()
					score += len(set(list1).intersection(set(list2)))/float(len(set(list1).union(set(list2))))
			scoreList.append([tableList[t1][0],(score*0.7+0.3*cosine1)])
	finalScoreList.append([tableList[t][0],scoreList])
for i in range(len(finalScoreList)):
	print finalScoreList[i]