from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Book, Review, Author


# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context ={
        "books": book_list
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')