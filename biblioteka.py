import sqlite3

conn = sqlite3.connect('biblioteka.db')
print("Datubāze ir izveidota!")

print("Dati ir veiksmīgi nolasīti!")

conn.execute('''CREATE TABLE COMPANY
             (INNER JOIN SELECT KEY  NOT NULL,
             NOSAUKUMS           TEXT NOT NULL,
             GADS           INT  NOT NULL,
             VARDS        CHAR(50),
             UZVARDS        REAL);''')
print("Tabula ir izveidota!")

conn.execute("INSERT INTO GRAMATA(NOSAUKUMS, GADS, VARDS, UZVARDS, SALARY) \
      VALUES (1, 'GRAMATA', 23, JAROSLAV, VOLKOV)")



cursor=conn.execute("SELECT * from GRAMATA")
for ieraksts in cursor:
  print("Kopēju izmaiņu skaits :", conn.total_changes)
conn.commit()
print("Ieraksti ir izveidoti")
conn.close()