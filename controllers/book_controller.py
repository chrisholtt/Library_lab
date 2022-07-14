from flask import Flask, render_template, redirect, Blueprint, request
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# # INDEX 
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)

# VIEW BOOK
@books_blueprint.route('/book/<id>')
def book(id):
    book = book_repository.select(id)
    # author = author_repository.select(book.author.id)
    return render_template('books/book.html', book=book)


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
    book_repository.save(book)
    return redirect('/books')


# EDIT BOOK
@books_blueprint.route("/books/edit/<id>", methods=["GET"])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book=book, authors=authors)


# UPDATE BOOK
@books_blueprint.route("/book/update/<id>", methods=["POST"])
def update_book(id):
    title = request.form['title']
    pages = request.form['pages']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(author, title, pages, id)
    book_repository.update(book)
    return redirect('/books')


# DELETING A BOOK
@books_blueprint.route("/book/delete/<id>", methods=["POST"])
def delete(id):
    book = book_repository.select(id)
    book_repository.delete(book)
    return redirect('/books')