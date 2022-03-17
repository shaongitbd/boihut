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
from checkout.views import checkout_req, checkout_page
from bookstore.views import orders
from bookstore.views import view_order
from bookstore.views import view_invoice
from accounts.views import profile_edit
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
    path('checkout', checkout_page, name="checkout_page"),
    path('checkout_req/process', checkout_req, name="checkout_req"),
    path("dashboard/", account_home, name="dashboard"),
    path('dashboard/orders',orders,name="orders"),
    path('dashboard/profile_edit', profile_edit,name="profile_edit"),
    path("dashboard/view_order/<int:order_id>", view_order, name="view_order"),
    path("dashboard/view_invoice/<int:invoice_id>", view_invoice,name="view_invoice"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)