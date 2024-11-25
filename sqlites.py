import sqlite3


conn = sqlite3.connect('rieksti.db')
cursor = conn.cursor()




cursor.execute('''
SELECT      
     vards, datums, nosaukums, cena, daudzums
            FROM
               Detalas
            Join
               pasutijums on Detalas.pasutijuma_id = pasutijums.pasutijuma_id
            Join
               Klients on Klients.klienta_id = pasutijums.klienta_id
            Join
               produkts on produkts.produkts_id = Detalas.produkta_id






''')


produkts_id = int(input("Ievadi produkta ID: "))
nosaukums = str(input("Ievadi produkta nosaukuma: "))
cena = float(input("Ievadi produkta cenu: "))
noliktava = bool(input("Ievadi noliktavas statusu (piemēram, 'ir' vai 'nav'): "))

cursor.exucute('''
INSERT INTO Produkti (produkts_id, nosaukums, cena, noliktava
VALUES (?, ?, ?, ?)
''', (produkts_id, nosaukums, cena, noliktava))

print("Produkts pievienots!") 

orders = cursor.fetchall()
print("Pasūtījumi:")
for order in orders:
    print(order)