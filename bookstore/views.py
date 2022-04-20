from django.shortcuts import render,get_object_or_404
from .models import Book
from category.models import Category
from checkout.models import order_list
from checkout.models import order
from checkout.models import invoice
from accounts.models  import Account
from checkout.models import invoice
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

categories_list = Category.objects.all()


#adding paging


def home(request):

    books = Book.objects.all()[0:20]
    font_page_context = {
        'books': books,
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


@login_required(login_url="/login")
def orders(request):
        if request.user.is_authenticated:
            user = Account.objects.get(email=request.user.email)
            order_id = order.objects.all().filter(client=user)

            all_orders = Paginator(order.objects.all().filter(client=user), 10)
            page = request.GET.get('page')

            try:
                orders = all_orders.page(page)
            except PageNotAnInteger:
                orders = all_orders.page(1)
            except EmptyPage:
                orders=  all_orders.page(all_orders.num_pages)

            context={

                'order_id_list' : orders,
            }
            return render(request,"list-orders.html",context)
        else:
            messages.error("Sorry, you need to be logged in to view your orders")
            return redirect("login")

@login_required(login_url="/login")
def view_order(request, order_id):
      if request.user.is_authenticated:

          print(order_id)
          order_items_list = order_list.objects.all().filter(order_id=order_id)
          invoice_details = invoice.objects.all().filter(order_id=order_id)



          context={
              "order_id":order_id,

              "order_items_list":order_items_list,
              "invoice_list": invoice_details
          }
          return render(request,"view_order.html",context=context)
      else:
          return redirect('login')


@login_required(login_url="/login")
def view_invoice(request, invoice_id):
     if request.user.is_authenticated:
         invoice_dat = invoice.objects.get(invoice_id=invoice_id)

         context = {

             'invoice':invoice_dat

         }
         return render(request,"view_invoice.html",context=context)
     else:
         return redirect("login")




