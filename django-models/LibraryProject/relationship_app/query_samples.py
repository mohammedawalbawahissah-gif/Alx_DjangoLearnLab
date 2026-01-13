from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author"""
    author = Author.objects.get(name=author_name)
    return author.books.all()

# Query all books by a specific author
author = Author.objects.first()
books_by_author = Book.objects.filter(author=author)

print(books_by_author)

def list_books_in_library(library_name):
    """List all books in a library"""
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    library = Library.objects.get(name=library_name)
    return library.librarian

from relationship_app.models import Author, Book
