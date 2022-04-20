from django.shortcuts import render,get_object_or_404
from bookstore.models import Book
from .models import Category
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage


categories_list = Category.objects.all()


def category(request, cat_slug=None):
    categories = None
    all_books = Paginator(Book.objects.all(),20)
    page = request.GET.get('page')
    books = all_books.page(page)

    context = {
        'books': books,
        'categories_list': categories_list

    }
    return render(request,'books-cat.html', context)


