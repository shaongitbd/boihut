from django.db import models

# Create your models here.
from bookstore.models import Book
from accounts.models import Account

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Account, on_delete = models.CASCADE)
    status = [("DRAFT","Draft"),
               ("PENDING","Pending"),
              ("REJECTED","Rejected"),
              ("CANCELLED","Cancelled"),
              ("DELIVERED","Delivered"),
              ("COMPLETED","Completed")]
    order_status = models.CharField(max_length=30,blank=True,choices=status)
    date_created = models.DateTimeField(blank=False,auto_now_add=True)
    date_updated = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return str(self.order_id)






class order_list(models.Model):
    order_id = models.ForeignKey(order, blank=False,on_delete=models.DO_NOTHING)
    order_item = models.ForeignKey(Book, blank=False,on_delete=models.DO_NOTHING)
    order_quantity = models.IntegerField(blank=False)
    order_price = models.IntegerField(blank=False)
    def __str__(self):
        return str(self.order_item)



class order_note_admin(models.Model):
    order_id = models.ForeignKey(order,blank=False,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=3000,blank=True)






class invoice(models.Model):
    status = (("NOT_PAID","Not Paid")
              ,("PAID","Paid"),
              ("PENDING_PAY","Pending Payment"),
              ("REJECTED","Rejected"),
              ("FRAUD","Fraud"),
              ("TIMEOUT","Timeout"))
    invoice_id = models.AutoField(primary_key=True, blank=False,unique=True)
    invoice_status = models.CharField(max_length=300, blank=False, choices=status,default="Pending Payment")
    order_id =models.ForeignKey(order, blank=False,on_delete=models.DO_NOTHING)
    total_price = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    """ billing Details - 
    Decided to put it here because Most website use it this way """

    first_name=models.CharField(max_length=70,blank=False)
    last_name=models.CharField(max_length=70,blank=False)
    address = models.CharField(max_length=500,blank=False)
    city = models.CharField(max_length=100,blank=False)
    division = models.CharField(max_length=60, blank=False)
    zip= models.CharField(max_length=60,blank=False)
    country = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return str(self.invoice_id)


