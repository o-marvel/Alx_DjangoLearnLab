from relationship_app.models import Author, Book, Library, Librarian


# def query_books_by_author(author_name):
#     """
#     Query all books written by a specific author
#     """
#     try:
#         author = Author.objects.get(name=author_name)
#         books = Book.objects.filter(author=author)

#         print(f"Books by {author.name}:")
#         for book in books:
#             print(f"- {book.title}")

#     except Author.DoesNotExist:
#         print("Author not found")


# def query_books_in_library(library_name):
#     """
#     List all books in a library
#     """
#     try:
#         library = Library.objects.get(name=library_name)
#         books = library.books.all()

#         print(f"Books in {library.name}:")
#         for book in books:
#             print(f"- {book.title}")

#     except Library.DoesNotExist:
#         print("Library not found")


# def query_librarian_for_library(library_name):
#     """
#     Retrieve the librarian for a library
#     """
#     try:
#         library = Library.objects.get(name=library_name)
#         librarian = library.librarian

#         print(f"Librarian for {library.name}: {librarian.name}")

#     except Library.DoesNotExist:
#         print("Library not found")
#     except Librarian.DoesNotExist:
#         print("No librarian assigned to this library")


# Example usage (run from Django shell or custom command)
# query_books_by_author("Chinua Achebe")
# query_books_in_library("Central Library")
# query_librarian_for_library("Central Library")

# query_samples.py

from relationship_app.models import Library, Book, Author, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Assuming `books` is a ManyToManyField in Library
        return books
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

# 3. Retrieve the librarian for a library by querying Librarian model directly
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Explicitly using Librarian.objects.get with library instance
        return librarian
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian found for the library {library_name}"

# Sample outputs for testing
if __name__ == "__main__":
    print(get_books_by_author("George Orwell"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))