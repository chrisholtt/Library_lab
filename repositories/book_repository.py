from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository


def save(book):
    sql = """
    INSERT INTO books (title, pages, author_id)
    VALUES (%s, %s, %s)
    RETURNING *
    """
    values = [book.title, book.pages, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    
    return book
    

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        results = results[0]
        author = author_repository.select(results['user_id'])
        book = Book(author, results['title'], results['pages'], results['id'] )
    return book


def select_all():
    books = []

    sql =  """
    SELECT * FROM books
    """
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(author, row['title'], row['pages'], row['id'] )
        books.append(book)

    return books


