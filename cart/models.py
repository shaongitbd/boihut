from django.db import models
from bookstore.models import Book
# Create your models here.

class Cart(models.Model):
    cart_session = models.CharField(max_length=250,null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)






class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField()


