import sqlite3
import pandas as pd
import pathlib

conn = sqlite3.connect('db.db')

for file_path in pathlib.Path('./tables').iterdir():
    df = pd.read_csv(file_path)
    df.to_sql(name=file_path.stem, con=conn, if_exists='replace', index=False)

f = open('query.sql')
query = f.read()
f.close()

print(pd.read_sql_query(query, conn))
