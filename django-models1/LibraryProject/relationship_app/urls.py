from django.urls import path
# from django.contrib.auth.views import views as auth_views
from .views import LibraryDetailView
from .views import list_books
from . import views    

# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import  LoginView, LogoutView



urlpatterns = [
    path("books/", list_books, name="book-list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
     # Login view with custom template

   path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    
    # Logout view with custom template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Register view
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]

