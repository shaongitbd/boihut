"""boihut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookstore.views import home
from bookstore.views import contact
from bookstore.views import about
from django.conf.urls.static import static
from django.conf import settings
from category.views import category
from bookstore.views import single_book
from cart.views import add_to_cart
from cart.views import cart
from cart.views import delete_cart_item
from cart.views import update_cart_item
from bookstore.views import search_result
from accounts.views import register
from accounts.views import login
from accounts.views import logout
from accounts.views import account_home
from checkout.views import checkout_req

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('contact',contact),
    path('about',about),
    path('category/<slug:cat_slug>/',category),
    path('book/<slug:single_book_slug>', single_book),
    path('cart/', cart,name = 'cart'),
    path('add_to_cart/<str:user_book>', add_to_cart,name="add_cart"),
    path('update_cart_item/<str:book_slug>', update_cart_item, name="update_cart"),
    path('delete_cart_item/<str:book_slug>', delete_cart_item, name="delete_cart_item"),
    path('search/', search_result, name="search_res"),
    path('register',register, name="register" ),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('account/home', account_home, name="account_home"),
    path('checkout/', checkout_req, name="checkout")


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)