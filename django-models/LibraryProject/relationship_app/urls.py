from django.urls import path
from django.contrib.auth.views import views as auth_views
from .views import LibraryDetailView
from .views import list_books

from . import views    

# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import  LoginView, LogoutView


urlpatterns = [
    path("books/", list_books, name="book-list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
]



urlpatterns = [
    # Login view with custom template
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout view with custom template
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Register view
    path('register/', views.register, name='register'),
]
