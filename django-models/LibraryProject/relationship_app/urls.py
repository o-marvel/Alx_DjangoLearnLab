from django.urls import path
from .views import LibraryDetailView, list_books

# urlpatterns = [
#     path("books/", view=views.list_books, name="book-list"),
# ]
urlpatterns = [
    path("books/", list_books, name="book-list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
]