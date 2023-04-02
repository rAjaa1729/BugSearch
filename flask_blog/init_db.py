import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "142857",
    database = "db"
)
cur = mydb.cursor()
# import sqlite3
# connection = sqlite3.connect('database.db')
# with open('schema.sql') as f:
#     connection.executescript(f.read())
# cur = connection.cursor()
cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('First Post', 'Content for the first post')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('Second Post', 'Content for the second post')
            )
mydb.commit()
mydb.close()