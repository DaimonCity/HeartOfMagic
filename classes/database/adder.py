import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
sqlite_connection = sqlite3.connect('example.db')
cursor.execute("INSERT INTO users (name, amount) VALUES ('xp', 250)")  # <- вот здесь менять что добавлять
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
