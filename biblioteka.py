import sqlite3

conn = sqlite3.connect('biblioteka.db')
print("Datubāze ir izveidota!")

print("Dati ir veiksmīgi nolasīti!")

conn.execute('''CREATE TABLE GRAMATA
             (ID INT PRIMATY KEY  NOT NULL,
             NOSAUKUMS           TEXT NOT NULL,
             GADS           INT  NOT NULL,
             VARDS        CHAR(50),
             UZVARDS        REAL);''')
print("Tabula ir izveidota!")

print("Kopēju izmaiņu skaits :", conn.total_changes)
conn.commit()
print("Ieraksti ir izveidoti")
conn.close()