import pandas as pd
import copy
import math
df = pd.read_csv('database.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

new = df.columns
newer = []
for i in range(len(new)):
	newer.append(new[i].replace(' ','_'))

df.columns = newer


new = copy.deepcopy(df)
for i in range(len(new['year'])):


	if len(new['year'][i])>4:
		new['year'][i] = new['year'][i][5:]

df = new

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:outlander@localhost:5432/dbproject')

df.to_sql("academy", engine)

