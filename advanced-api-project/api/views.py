from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer

# ==========================
# LIST VIEW (Public)
# ==========================
class BookListView(generics.ListAPIView):
    """
    Retrieves all books.
    Public endpoint (no authentication required).
    Supports filtering and searching.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Filtering & searching
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']


# ==========================
# DETAIL VIEW (Public)
# ==========================
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Public endpoint.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ==========================
# CREATE VIEW (Protected)
# ==========================
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users can create books.
    Includes validation handling.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook to control object creation.
        Ensures validation runs and allows future extension
        (e.g logging, ownership, audit tracking).
        """
        serializer.save()


# ==========================
# UPDATE VIEW (Protected)
# ==========================
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom update hook.
        Can be extended for versioning, audit logs, etc.
        """
        serializer.save()


# ==========================
# DELETE VIEW (Protected)
# ==========================
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
