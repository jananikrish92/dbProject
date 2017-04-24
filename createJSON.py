import json
from pprint import pprint
import psycopg2 as py
try:
	conn = py.connect("dbname = 'dbproj' user = 'postgres' host = 'localhost' port='5433' password = 'db123'")
except:
	print "I cannot connect to db"
cur = conn.cursor()
data = []
with open('sample.json') as f:
    for line in f:
        data.append(json.loads(line))

for i in range(len(data)):
	if data[i]["tableOrientation"] == "HORIZONTAL":
		for j,val in enumerate(data[i]):
			if val == "relation":
				# import pdb 
				# pdb.set_trace()
				for k in range(len(data[i][val])):
					arrayList = data[i][val][k]
					# import pdb
					# pdb.set_trace()
					if k == 0:
						str1 =""
						for value in range(len(arrayList)):
							if arrayList[value] == "":
								arrayList[value] = 'attribute'+str(value)
							else:
								str2 = arrayList[value]
								arrayList[value] = str2.replace(" ","_")
							str1 = str1+arrayList[value]+" text,"
						str1 = str1[:-1]
						import pdb 
						pdb.set_trace()	
						cur.execute("""create table relation"""+str(i)+"""("""+str1+""");""")
					else:
						print "i have values"
	else:
		print "vertical"