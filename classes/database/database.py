import sqlite3

# создаем соединение с нашей базой данных
conn = sqlite3.connect('stats.db')
cursor = conn.cursor()

# получаем метаданные для таблицы
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
