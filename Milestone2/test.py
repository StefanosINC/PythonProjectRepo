import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor() ## Used to execute sql querie

cursor.execute('Your sql query here')
connection.commit()
connection.close()