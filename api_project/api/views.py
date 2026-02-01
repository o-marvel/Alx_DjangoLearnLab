from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ login required


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAdminUser]  # ✅ admin only

class BookViewSet(viewsets.ModelViewSet):
    """
    Book API ViewSet

    Authentication:
    - TokenAuthentication is enabled globally in settings.py

    Permissions:
    - Only authenticated users can access this endpoint

    Endpoints:
    - GET /api/books_all/
    - POST /api/books_all/
    - PUT /api/books_all/<id>/
    - DELETE /api/books_all/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

