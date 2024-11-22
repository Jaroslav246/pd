import sqlite3


conn = sqlite3.connect('Interneta_veikals.db')
cursor = conn.cursor()




cursor.execute('SELECT * FROM Pasutiijumi')
orders = cursor.fetchall()
print("Pasūtījumi:")
for order in orders:
    print(order)