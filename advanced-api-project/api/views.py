from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# ==========================
# List all books
# GET /api/books/
# ==========================
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books in the system.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ==========================
# Retrieve a single book
# GET /api/books/<id>/
# ==========================
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


# ==========================
# Create a new book
# POST /api/books/create/
# ==========================
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book record.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ==========================
# Update an existing book
# PUT /api/books/<id>/update/
# ==========================
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"


# ==========================
# Delete a book
# DELETE /api/books/<id>/delete/
# ==========================
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"
