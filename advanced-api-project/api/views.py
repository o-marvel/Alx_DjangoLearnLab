from django.shortcuts import render
#from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from django_filters import rest_framework
from rest_framework import generics
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



from .serializers import BookSerializer
from .models import Book

class BookListView(generics.ListAPIView):
    """Return a list of all books."""
    permission_classes = [IsAuthenticatedOrReadOnly]

    # filter_backends = [
    #     rest_framework.DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter,
    # ]

     # Enable filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Step 1: Filtering fields
    filterset_fields = [
        'title',
        'author',
        'publication_year'
    ]

    # Step 2: Search fields
    search_fields = [
        'title',
        'author__name'   # if Author is a ForeignKey
    ]

    # Step 3: Ordering fields
    ordering_fields = [
        'title',
        'publication_year'
    ]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetailView(generics.RetrieveAPIView):
    """Return details of a single book."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    """Allow authenticated users to create a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookUpdateView(generics.UpdateAPIView):
    """Allow authenticated users to update a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookDeleteView(generics.DestroyAPIView):
    """Allow authenticated users to delete a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer