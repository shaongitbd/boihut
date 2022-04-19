from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth,messages
from cart.models import Cart,CartItems
from .models import order,order_list,order_note_admin,invoice
from bookstore.models import Book
from django.contrib.auth.decorators import  login_required

@login_required(login_url="/login")
def checkout_req(request):

    special_char_list = r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    email_special_char_list = r"!\"#$%&'()*+,/:;<=>?@[\]^`{|}~"

    def num_checker(string):
        return any(i.isdigit() for i in string)

    def special_char_checker(string):
        for i in string:
            if i in special_char_list:
                return True
        return False

    def email_special_char_checker(string):
        if "@" in string:
            email = string.split("@", "")
            for i in email[0]:
                if i in email_special_char_list:
                    return True
            return False
        else:
            return True

    if request.POST:
        req_user = request.user

        if req_user.is_authenticated:

            #checking if transaction ID alreay exits in db

            transaction_id = request.POST['transaction_id']
            invoice_exits = invoice.objects.filter(transaction_id=transaction_id).exists()

            if invoice_exits == True:
                messages.error(request,"Sorry, transaction Id alreay exits.")
                return redirect("checkout_page")


            # working on order model

            client = request.user
            print(client)
            order_note = request.POST['order_note']
            # Unsafe to grab total from get or post req
            # So, I think it's bettter for me to comment out this line.
            # But I could have used it because it's a university project
            # and not many people is going to use it in their production environment. Feel free to use if if you like

            # total = request.POST['total']


            order_save = order.objects.create(
                client=client,
               # order_note_user=order_note,

            )
            order_save.save()

            # working on order_list


            session = request.session.session_key

            cart = Cart.objects.get(cart_session=session)
            print(cart)
            cart_items_list = CartItems.objects.all().filter(cart=cart)
            print(cart_items_list)
            total = 0
            print(order_save)

            for item in cart_items_list:

                order_item= Book.objects.get(title=item.book)
                price = order_item.price
                quantity = item.quantity
                total += price*quantity

                order_list_save = order_list.objects.create(
                    order_id=order_save,
                    order_item=order_item,
                    order_price=price,
                    order_quantity=quantity
                )
                order_list_save.save()

            # working on invoice


            total_price = total
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            city = request.POST['city']
            division = request.POST['division']
            zip = request.POST['zip']
            country = request.POST['country']
            order_note = request.POST['order_note']

            # Chcking for any invalid/ suspecious inputs

            # Checking for number

            if num_checker(first_name) == True:
                messages.error(request, "Sorry, First Name can't contain number")
                return redirect("checkout_page")

            if num_checker(last_name) == True:
                messages.error(request, "Sorry, Last Name can't contain number")
                return redirect("checkout_page")

            if num_checker(division) == True:
                messages.error(request, "Sorry, Division can't contain a number")
                return redirect("checkout_page")

            if num_checker(city) == True:
                messages.error(request, "Sorry, City can't contain number")
                return redirect("checkout_page")

            if num_checker(country) == True:
                messages.error(request, "Sorry, Country Name can't contain number")
                return redirect("checkout_page")

            # Checking for special character

            if special_char_checker(first_name):
                messages.error(request, "Sorry, First Name can't contain a special character.")
                return redirect("checkout_page")

            if special_char_checker(last_name):
                messages.error(request, "Sorry, Last Name can't contain a special character.")
                return redirect("checkout_page")

            if special_char_checker(division):
                messages.error(request, "Sorry, Division can't contain a special character.")
                return redirect("checkout_page")

            if email_special_char_checker(city):
                messages.error(request, "Sorry, City  can't contain a special character.")
                return redirect("checkout_page")

            if email_special_char_checker(country):
                messages.error(request, "Sorry, Country can't contain a special character.")
                return redirect("checkout_page")

            save_invoice = invoice.objects.create(
                order_id=order_save,
                total_price=total_price,
                first_name=first_name,
                last_name=last_name,
                address=address,
                division=division,
                city=city,
                zip=zip,
                country=country,
                transaction_id=transaction_id,
                order_note=order_note,
                transaction_method = 'bkash',
                invoice_status="PENDING_CHECK",


            )
            # updating order

            order_status_update = order.objects.filter(order_id=order_save.order_id).update(order_status="PROCESSING")
            # removing cart
            cart.delete()
            messages.success(request,"Your order has been successfully received.")
            return redirect("orders")


        else:
            return redirect("login")



def checkout_page(request):
    if request.user.is_authenticated:
        return render(request, "checkout.html")
    else:
        messages.error(request,"You need to be registered to place an order ")
        return redirect("register")

