import sqlite3

connection = sqlite3.connect('shop_db.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('INSERT INTO items (title, price) VALUES (?, ?)',
            ('First product', 345)
            )

cur.execute('INSERT INTO items (title, price) VALUES (?, ?)',
            ('Second product', 23999)
            )

connection.commit()
connection.close()