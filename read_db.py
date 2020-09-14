import sqlite3
import pandas as pd
conn=sqlite3.connect('mechmaster.db')
df = pd.read_sql("select * from mechmaster_test",con=conn)
print(df.head())


#c= conn.cursor()
#b = c.execute(""" SELECT * FROM mechmaster_test
#""").fetchall()
#print(b)
#conn.commit()
#conn.close()
