from django.db import models
from bookstore.models import Book
# Create your models here.

class Cart(models.Model):
    cart_session = models.CharField(max_length=250)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_session


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField()


