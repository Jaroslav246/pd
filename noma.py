import sqlite3 as db 

with db.connect('nomat.db') as con:
  cur = con.cursor()
  
  cur.execute(""" SELECT  Nomnieks.vards, Nomnieks.uzvards, Noma.beig_datums
              FROM Nomnieks
              INNER JOIN Noma
              ON Noma.id_nomnieks = Nomnieks.id_nomnieks 
              WHERE Nomnieks.tel_nr = '26543219' 
              """)
  nomniek = cur.fetchall()

print("Izdrukā datumus, kuros klientam ar telefona nr '26543219' jaatdot produkti:")
for rinda in nomniek:
  print (rinda)


  
