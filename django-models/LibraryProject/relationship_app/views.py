# relationship_app/views.py

from django.shortcuts import render
from .models import Book  # Adjust the model import as needed

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library  # Adjust the model import as needed

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect("book-list")  # redirect after successful registration
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})