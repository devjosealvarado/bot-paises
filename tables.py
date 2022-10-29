import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
# Creacion de tablas SQL
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        discord_id TEXT PRIMARY KEY,
        name TEXT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        country_id INTEGER PRIMARY KEY,
        discord_id TEXT,
        country TEXT,
        FOREIGN KEY (discord_id)
            REFERENCES users (discord_id)
    )
''')
con.commit()