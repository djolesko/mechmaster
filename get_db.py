#get sqlite3

import sqlite3

conn=sqlite3.connect('mechmaster.db')
c= conn.cursor()
c.execute(""" INSERT INTO mechmaster_test(ime,prezime,datum,opis) VALUES(?,?,?,?)
""",('djordje','papaz','05-07-1988','mali servis'))
conn.commit()
conn.close()