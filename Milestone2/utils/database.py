import json
from .Database_connection import DataBaseConnection
books_file = 'books.txt'


def create_book_table():
    with DataBaseConnection() as connection: ## { Connection is whatever the DUNDER __Enter__ method returned}
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)') #Table

    #connection.commit() # Push the DB.
   # connection.close() # Close the connection


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books') # Execute this

# This allows us to end iwth a dictionary
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] ## you wil get a list of tuples. [(name, author, read), (name, author, read)]
    

    connection.close()
    return books
def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author)) #This is saafer

    connection.commit() # Push the DB.
    connection.close() # Close the conn

def mark_book_as_read(name):
    ## mark all books as read
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name)) ## Update the book where the name is equal
    connection.commit()
    connection.close()

def delete_book(name):
    ## mark all books as read
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (name)) ## Update the book where the name is equal
    connection.commit()
    connection.close()