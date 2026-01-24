from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("You can create a book")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You can delete a book")

