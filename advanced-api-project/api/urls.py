from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

"""
API Routing Configuration for Book CRUD operations
"""

urlpatterns = [
    path("books/list", BookListView.as_view(), name="book-list"),
    path("books/create", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),
    # READ (Public)
    # path("books/", BookListView.as_view(), name="book-list"),
    # path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # # CREATE (Protected)
    # path("books/create/", BookCreateView.as_view(), name="book-create"),

    # # UPDATE (Protected)
    # path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),

    # # DELETE (Protected)
    # path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
