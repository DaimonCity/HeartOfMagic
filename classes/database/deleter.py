import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
sqlite_connection = sqlite3.connect('example.db')
cursor.execute("DELETE FROM users WHERE name = 'new_weapon_found'")
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)