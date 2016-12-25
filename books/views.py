from django.shortcuts import render
from books.models import Book, Review, Author
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context ={
        "books": book_list
    }

    return render(request, 'index.html', context)