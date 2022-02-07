from django.db import models

# Create your models here.
from bookstore.models import Book
from account.models import Account

class order(models.Model):
    order_id = models.AutoField(unique=True)
    client = models.ForeignKey(Account,blank=False,on_delete=models.DO_NOTHING)
    status = ("Draft","Pending","Rejected","Cancelled","Delivered","Completed")
    order_status = models.CharField(max_length="30",blank=False,choices=status,default="Draft")
    invoice_id = models.ForeignKey('invoice', on_delete=models.DO_NOTHING)
    total = models.IntegerField(blank=False)
    date_created = models.DateTimeField(blank=False,auto_now_add=True)
    date_updated = models.DateTimeField(blank=False,auto_now=True)
    order_note_user = models.CharField(max_length=2000,blank=True)
    order_note_admin = models.ForeignKey('order_notes_admin', on_delete=models.DO_NOTHING)



class order_list(models.Model):
    order_id = models.ForeignKey(order, blank=False,on_delete=models.DO_NOTHING)
    order_item = models.ForeignKey(Book, blank=False)
    quantity = models.IntegerField(blank=False)
    price = models.ForeignKey(Book, blank=False)


class invoice(models.Model):
    status = ("Not Paid","Paid","Pending Payment","Rejected","Fraud","Timeout")
    invoice_id = models.AutoField(blank=False,unique=True)
    invoice_status = models.CharField(blank=False, choices=status,default="Pending Payment")
    order_id =models.ForeignKey(order, blank=False,on_delete=models.DO_NOTHING)
    total_price = models.ForeignKey(order,blank=False,on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeFiekd(auto_now=True)

    """ billing Details - 
    Decided to put it here because Most website use it this way """

    first_name=models.CharField(max_length=70,blank=False)
    last_name=models.CharField(max_kength=70,blank=False)
    address = models.CharField(max_length=500,blank=False)
    city = models.CharField(max_length=100,blank=False)
    Division = models.CharField(max_length=60, blank=False)
    zip= models.CharField(max_length=60,blank=False)
    country = models.CharField(max_length=100,blank=True)


class order_note_admin(models.Model):
    order_id = models.ForeignKey(order,blank=False,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=3000,blank=True)