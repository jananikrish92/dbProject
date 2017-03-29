import pandas as pd
df = pd.read_csv('archive.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
new = df.columns.values
new[7] = 'fullname'
df.columns = new
print df.columns[7]

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:outlander@localhost:5432/nobel_l')

df.to_sql("nobel", engine)
