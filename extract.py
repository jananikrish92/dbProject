import psycopg2 as py

try:
	conn = py.connect("dbname = 'nobel_l' user = 'postgres' host = 'localhost' port='5433' password = 'db123'")
except:
	print "I cannot connect to db"
cur = conn.cursor()
cur.execute("""select column_name,table_name from temp;""")
row1 = cur.fetchall()

lis = []
for i in range(len(row1)):
	
	cur.execute("""select """+row1[i][0]+""" from """+row1[i][1]+""";""")
	row2 = cur.fetchall()
	lis.append(row2)


sql = 'insert into index_table(value,column_name,table_name)values(%s,%s,%s)'
		
print len(row1)
print len(lis[0])
errors = []
count =0
for i in range(len(row1)):
	for j in range(len(lis[i])):
			if lis[i][j][0]!=None:
				try:
					cur.execute(sql, (str(lis[i][j][0]),str(row1[i][0]),str(row1[i][1])))
					conn.commit()	
				except:
					print 'hi'
					errors.append([str(lis[i][j][0]),row1[i][0],row1[i][1]])
				#print row1[i][0],row1[i][1],lis[i][j][0]
				count=count+1

print count
