import mysql.connector
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sql@Prism1920",
    database = "posts"
)
cursor = connection.cursor()

cursor.execute("INSERT INTO post (title, content) VALUES (%s, %s)",
            ('First Post', 'Content for the first post')
            )
cursor.execute("INSERT INTO post (title, content) VALUES (%s, %s)",
            ('Second Post', 'Content for the second post')
            )
connection.commit()
cursor.close()
connection.close()

