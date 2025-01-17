import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
sqlite_connection = sqlite3.connect('example.db')
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)