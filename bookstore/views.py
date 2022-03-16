from django.shortcuts import render,get_object_or_404
from .models import Book
from category.models import Category
from checkout.models import order_list
from checkout.models import order
from accounts.models  import Account
from checkout.models import invoice

categories_list = Category.objects.all()


# :/ ektu beshi e kosto kora lage eida te

def home(request):
    books = Book.objects.all()[0:20]
    font_page_context = {
        'books': books,
         'categories_list': categories_list,
          'agent':request.META['HTTP_USER_AGENT'],

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


def search_result(request):
    if 'query' in request.GET:
        q = request.GET['query']
        books = Book.objects.all().filter(title=q)
        print(q)
        print(books)
        context  = {
            'books':books,
        }
        return render(request, 'search_res.html', context)



def orders(request):
        if request.user.is_authenticated:
            print("working")
            user = Account.objects.get(email=request.user.email)
            order_id = order.objects.all().filter(client=user)
            context={

                'order_id_list' : order_id,
            }
            return render(request,"dashboard.html",context)


def view_order(request, order_id):
      if request.user.is_authenticated:

          print(order_id)
          order_items_list = order_list.objects.all().filter(order_id=order_id)

          context={

              "order_items_list":order_items_list,
          }
          return render(request,"view_order.html",context=context)



def view_invoice(request, invoice_id):
     if request.user.is_authenticated:
         invoice_dat = invoice.objects.get(invoice_id=invoice_id)

         context = {

             'invoice':invoice_dat,

         }
         return render(request,"view_invoice.html",context=context)
