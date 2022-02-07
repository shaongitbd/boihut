from django.shortcuts import render,redirect
from cart.models import Cart,CartItems
from .models import order,order_list,order_note_admin,invoice


def checkout_req(request):
    if request.POST:
        req_user = request.user
        if req_user.is_authenticated:
            # working on order model
            client = request.user
            order_note = request.POST['order_note']

            # Unsafe to grab total from get or post req
            # So, I think it's bettter for me to comment out this line.
            # But I could have used it because it's a university project
            # and not many people is going to use it in their production environment. Feel free to use if if you like

            # total = request.POST['total']


            order_save = order.create(
                client=client,
                order_note_user=order_note,

            )
            order_save.save()

            # working on order_list

            order_id = order.objects.get(order_save.id)

            session = request.session.session_key
            cart = Cart.objects.get(cart_session=session)
            cart_items_list = CartItems.objects.all().filter(cart=cart)
            total = 0

            for item in cart_items_list:

                order_item_z= Book.objects.get(title=item.title)
                price_z = item.price
                quantity = item.quantity
                total += price*quantity

                order_list_save = order_list.create(
                    order_id=order_id,
                    order_item=order_item_z,
                    order_price=price_Z,
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
            country = reqeust.POST['country']



            save_invoice = invoice.save(
                total_price=total,
                first_name=first_name,
                last_name=last_name,
                city=city,
                zip=zip,
                country=country,
            )
            save_invoice.save()

        else:
            return redirect("login")
    else:
        return redirect("register")


def checkout_page(request):
    if request.user.is_authenticated:
        return render(request, "checkout.html")
    else:
        return redirect("register")

