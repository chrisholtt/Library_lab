import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Jack", "Jarvis")
author_repository.save(author1)

author2 = Author("Javier", "Gonzalez")
author_repository.save(author2)

author_repository.select_all()

book1 = Book(author1, "Lord of the flies", 300)
book_repository.save(book1)

book2 = Book(author2, "Of Mice and Men", 250)
book_repository.save(book2)

# print(author_repository.select(1))


pdb.set_trace()
