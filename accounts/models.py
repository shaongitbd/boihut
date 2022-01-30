from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):

     def client_ip(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

     def create_user(self, first_name, last_name,username,phone, email,password):


       if not first_name:
           raise ValueError("You must provide Your First Name")
       if not username:
           raise ValueError("You must provide a username")
       if not email:
           raise ValueError("You must provide your email address")
       if not phone:
           raise ValueError("You must provide a phone number")

       user = self.model(
           email=self.normalize_email(email),
           first_name=first_name,
           last_name=last_name,
           username=username,
           phone=phone,

            )
       user.is_admin = False
       user.is_superadmin = False
       user.is_stuff = False
       user.is_active = True
       user.set_pasword(password)
       user.save(using=self.db)
       return user

     def create_admin_account(self, first_name, last_name,username,phone, email,password):
          if not first_name:
              raise ValueError("You must provide Your First Name")
          if not username:
              raise ValueError("You must provide a username")
          if not email:
              raise ValueError("You must provide your email address")
          if not phone:
              raise ValueError("You must provide a phone number")

          user = self.model(
              email=self.normalize_email(email),
              first_name=first_name,
              last_name=last_name,
              username=username,
              phone=phone,

          )
          user.is_admin = True
          user.is_superadmin = True
          user.is_stuff = True
          user.is_active = True
          user.set_pasword(password)
          user.save(using=self.db)
          return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100,unique=True)

    registered_on = models.DateTimeField(auto_now=True)
    last_active = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    #registration_ip = models.CharField(max_length=100,blank=False)
    #last_login_ip = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','email','username','phone']
    objects = AccountManager()
    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perm(self, add_label):
        return True

