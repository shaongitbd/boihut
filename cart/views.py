from django.shortcuts import render,get_object_or_404,redirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from .models import Cart
from .models import CartItems
from bookstore.models import Book



def add_to_cart(request, user_book):
    session  = request.session.session_key


    if not session:
        session = request.session.create()
        session = request.session.session_key

        cart_for_save = Cart.objects.create(
          cart_session=session,
         )
        cart_for_save.save()


    #user_book=Book.objects.get(slug=user_book)
    session_aa = Cart.objects.get(cart_session=session)
    op_book = Book.objects.get(slug=user_book)

    check_if_already_exits = CartItems.objects.all().filter(cart=session_aa, book=op_book).first()
    print(check_if_already_exits)


    if check_if_already_exits == None:


        cartitem_save = CartItems.objects.create(
          cart= Cart.objects.get(cart_session=session),
          book= Book.objects.get(slug=user_book),
          quantity=1,
          is_active=True,
          )
        cartitem_save.save()

    else:
        quantity_update = CartItems.objects.get(cart=session_aa, book=op_book)
        quantity_update = quantity_update.quantity+1

        cartitem_save = CartItems.objects.update(
            cart=Cart.objects.get(cart_session=session),
            book=Book.objects.get(slug=user_book),
            quantity=quantity_update,
            is_active=True,
        )
        cartitem_save.save()


    return redirect('cart')


def delete_cart_item(request, book_slug):
    session = request.session.session_key
    my_cart = Cart.objects.get(cart_session=session)
    cart_items = CartItems.objects.all().filter(cart=my_cart)
    for cart_item in cart_items:

        if cart_item.book.slug==book_slug:
            print(cart_item)
            cart_item.delete()






    return redirect('cart')


def cart(request):
    session = request.session.session_key
    cart_num = Cart.objects.get(cart_session=session)
    cart_items = CartItems.objects.all().filter(cart=cart_num)
    total=0
    for cart_item in cart_items:
        total += cart_item.book.price
    context = {
        'cart_items': cart_items,
        'total':total,

    }

    return render(request, "cart.html", context)





