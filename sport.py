import sqlite3

conn = sqlite3.connect('sport.db')
print("Datubāze ir izveidota!") 

cursor=conn.execute("SELECT * from Abonement")
for ieraksts in cursor:
    print("SPORTA VEIDS= ", ieraksts[0])
    print("NODARBIBA= ", ieraksts[1])
    print("ABONEMENT= ", ieraksts[2])



print("Dati ir veiksmīgi nolasīti!")

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
'''conn.execute(CREATE TABLE Abonement
             (ID INT PRIMATY KEY  NOT NULL,
             NODARBIBA           TEXT NOT NULL,
             KLIENTS            INT  NOT NULL,
             VARDS        CHAR(50),
                      REAL);)
print("Tabula ir izveidota!")


conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (1, 'PAUL', 32, 'California', 20000.0 )")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (2, 'Alex', 25, 'Latvia', 15000.0 )")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.0 )")
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) \
      VALUES (4, 'Mark', 25, 'Germany', 65000.0 )")

conn.execute("UPDATE COMPANY set SALARY = 25000.0 where ID=1")
conn.commit()
print("Kopēju izmaiņu skaits :", conn.total_changes)

conn.commit()
print("Ieraksti ir izveidoti")'''
    )

'''def insert_data(conn, sporta veids, nodarbiba, abonement)
    cursor = conn.cursor()'''
print("Ieraksti ir izveidoti")
contact_name = input('Ievadiet Darbinieka vārdu: ')
contact_position = input('Darbinieka abonement: ')
contact_id = input('Darbinieka id: ')
sporta_zāle = input('1 dvieļa noma maksā 5 eiro: ')


id_abonement = int(input("Ievadi abonement ID: "))
nodarbiba = str(input("Ievadi nodarbiba nosaukuma: "))
cena = float(input("Ievadi produkta cenu: "))
sporta_veids = bool(input("Ievadi veids statusu (piemēram, 'ir' vai 'nav'): "))

cursor.exucute('''INSERT INTO Abonement (id_abonement, nodarbiba, sporta_veids VALUES (?, ?, ?)''', (id_abonement, nodarbiba, sporta_veids))

print("Abonement pievienots!") 

orders = cursor.fetchall()
print("Pasūtījumi:")
for order in orders:
   print(order)
conn.close()