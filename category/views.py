from django.shortcuts import render,get_object_or_404
from bookstore.models import Book
from .models import Category
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from category.models import Category



def category(request, cat_slug=None):
    cat_name = None
    if cat_slug is None:
        all_books = Paginator(Book.objects.all().order_by('-modified_on'),20)
    else:
        print(cat_slug)
        cat = Category.objects.get(slug=cat_slug)
        all_books = Paginator(Book.objects.all().filter(category=cat).order_by('-modified_on'),20)

    page = request.GET.get('page')

    try:
        books = all_books.page(page)
    except PageNotAnInteger:
        books = all_books.page(1)
    except EmptyPage:
        books = all_books.page(1)

    context = {
        'books': books,
    }
    return render(request,'books-cat.html', context)


