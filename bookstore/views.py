from django.shortcuts import render,get_object_or_404
from .models import Book
from category.models import Category
categories_list = Category.objects.all()

# :/ ektu beshi e kosto kora lage eida te

def home(request):
    books = Book.objects.all()[0:20]
    font_page_context = {
        'books': books,
         'categories_list': categories_list

    }
    return render(request, 'index.html',font_page_context)



def contact(request):


    return render(request, 'contact-us.html')

def about(request):

    return render(request, 'about.html')

def single_book(request, single_book_slug):
    if single_book_slug is not None:
        book = get_object_or_404(Book,slug=single_book_slug)


        #releated_categories = get_object_or_404(Category,slug=single_book_slug)
        releated_books = Book.objects.all().filter(category=book.category)[0:5]


        context = {

            'book': book,
             'related_books': releated_books,
             'categories_list': categories_list,

        }

    return render(request, 'book-single-page.html',context)
