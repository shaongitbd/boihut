from django.db import models
from category.models import Category


class Book(models.Model):
    title = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    image = models.ImageField(upload_to="images/books_img/")
    author = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=3000,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)
    stocks = models.IntegerField(blank=False)
    stocks_available = models.BooleanField(default=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
      return self.title


