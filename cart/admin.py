from django.contrib import admin
from .models import Cart,CartItems
# Register your models here.
admin.site.register(CartItems)
admin.site.register(Cart)
