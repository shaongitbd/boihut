from django.contrib import admin
from .models import order_note_admin,order,order_list,invoice
# Register your models here.
admin.site.register(order)
admin.site.register(order_list)
admin.site.register(order_note_admin)

admin.site.register(invoice)