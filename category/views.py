from django.shortcuts import render,get_object_or_404
from bookstore.models import Book
from .models import Category



categories_list = Category.objects.all()

def category(request, cat_slug=None):
    categories = None

    books = Book.objects.all()
    context = {
        'books': books,
        'categories_list': categories_list

    }
    return render(request,'books-cat.html', context)