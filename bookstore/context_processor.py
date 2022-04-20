from category.models import Category
from cart.models import Cart,CartItems

def header_infos(request):
    categories  = Category.objects.all()
    session = request.session.session_key
    total_cart_items = 0
    try:

        cartitem = CartItems.objects.all().filter(
            cart=Cart.objects.get(cart_session=session)
        )
        for i in cartitem:
            total_cart_items += i.quantity

    except:
        cart_for_save = Cart.objects.create(
            cart_session=session,
        )
        cart_for_save.save()

    return {
        'categories':categories,
         'total_cart_items':total_cart_items
    }

