from django.urls import path, include
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
      path('books/', include('bookshelf.urls')),
]


