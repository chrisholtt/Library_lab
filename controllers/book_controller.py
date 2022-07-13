from flask import Flask, render_template, redirect, Blueprint, request
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# # INDEX 
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    # authors = author_repository.select_all()
    return render_template("books/index.html", books=books)
    # had below being passed down
    # authors=authors


# new book page
@books_blueprint.route("/books/new")
def new_book_page():
    authors = author_repository.select_all()
    books = book_repository.select_all()
    return render_template('books/new.html', authors=authors, books=books)


# CREATE NEW BOOK
@books_blueprint.route("/books/new", methods=["POST"])
def create_book():
    title = request.form['title']
    pages = request.form['pages']
    id = request.form['id']
    author = author_repository.select(id)
    book = Book(author, title, pages, id)
    # author_repository.save(author)
    book_repository.save(book)
    return redirect('/books')



