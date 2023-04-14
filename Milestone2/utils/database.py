books_file = 'books.txt'


def create_book_table():
    pass


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readLine()] #Strip the white space
        return [{
            'name': line[0], 
            'author': line[1], 
            'read': line[3]
            }
            for line in lines
        ]


def insert_book(name, author):
    with open(books_file, 'a') as file: ## with A mode anything we write will goto the end of the file .  ( were appending)
        file.write(f'{name},{author}, 0')

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
    _save_all_books(books)

def _save_all_books(books):
    with open(books_file, 'w') as file: # Writing all the books. (Not best way but we are rewriting the file. )
        for book in books:
            file.write(f"{book['name']}, {book['author']} {book['read']}\n")

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book ['name'] != name]
    _save_all_books(books)


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)