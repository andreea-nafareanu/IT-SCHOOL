import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_FILE = ROOT / "db1.sqlite"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#rows = cursor.execute("SELECT * FROM users;")
#print(rows.fetchall())

email = input("Email: ")
name = input("Name: ")

cursor.execute("""INSERT INTO users (email, name) VALUES (?, ?);""", (email, name))

rows = cursor.execute("SELECT * FROM users;")

for row in rows:
    print(row)
