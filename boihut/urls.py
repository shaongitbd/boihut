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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('contact',contact),
    path('about',about),
    path('category/<slug:cat_slug>/',category),
    path('book/<slug:single_book_slug>', single_book)


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)