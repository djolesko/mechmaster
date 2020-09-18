#get sqlite3

import sqlite3

conn=sqlite3.connect('mechmaster.db')
c= conn.cursor()
c.execute(""" INSERT INTO mechmaster_test(iznos,faktura,kilometraza,napomene,model) VALUES(?,?,?,?,?)
""",('5000','255/20','135000','viljuska otisla','corsa'))
#conn.commit()
#conn.close()

#c.execute("""ALTER TABLE mechmaster_test
#	add column model text""")
conn.commit()
conn.close()