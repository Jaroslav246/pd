
import sqlite3

conn = sqlite3.connect('test.db')
print("Datubāze ir izveidota!") 

cursor=conn.execute("SELECT * from COMPANY")
for ieraksts in cursor:
    print("ID= ", ieraksts[0])
    print("NAME= ", ieraksts[1])
    print("ADDRESS= ", ieraksts[3])
    print("AGE= ", ieraksts[2])
    print("SALARY= ", ieraksts[4], "\n")
 
print("Dati ir veiksmīgi nolasīti!")


'''conn.execute(CREATE TABLE COMPANY
             (ID INT PRIMATY KEY  NOT NULL,
             NAME           TEXT NOT NULL,
             AGE            INT  NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);)
print("Tabula ir izveidota!")'''

'''conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (1, 'PAUL', 32, 'California', 20000.0 )")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (2, 'Alex', 25, 'Latvia', 15000.0 )")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.0 )")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (4, 'Mark', 25, 'Germany', 65000.0 )")

conn.commit()
print("Ieraksti ir izveidoti")'''
conn.close()