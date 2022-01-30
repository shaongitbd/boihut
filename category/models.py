from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=20,unique=True)
    category_image = models.ImageField(upload_to="images/cat/", blank=True)
    category_des = models.TextField(max_length=2000,blank=True)

    def __str__(self):
        return self.category_name
