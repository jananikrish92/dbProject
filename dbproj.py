import pandas as pd
df = pd.read_csv('archive.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
new = df.columns.values
for i in range(len(new)):
	if ' ' in new[i]:
		new[i] = new[i].replace(' ','_')

df.columns = new

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:outlander@localhost:5432/nobel_l')

df.to_sql("nobel", engine)
