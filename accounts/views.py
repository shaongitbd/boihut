from django.shortcuts import render,redirect
from .models import AccountManager,Account
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.


def register(request):
    x_forwarded_for = ''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.POST:

        post_username = request.POST['username']
        post_password = request.POST['password']
        post_conf_password =request.POST['confirm_password']
        post_email = request.POST['email']
        post_phone =  request.POST['phone']
        post_first_name = request.POST['first_name']
        post_last_name = request.POST['last_name']
        check_username = Account.objects.all().filter(username=post_username)
        check_email = Account.objects.all().filter(email=post_email)

        if post_password != post_conf_password:

            message.error(request, 'Password and Confirm Password Does not match')
            return redirect("register")

        if not check_username or not check_email:
            user = Account.objects.create(
                first_name=post_first_name,
                last_name=post_last_name,
                username=post_username,
                email=post_email,
                phone = post_phone,
            )
            user.set_password(post_password)
            print(post_password)



            user.save()
            print(ip)


            messages.success(request, 'Your account has been registered. Please Login now')
            return redirect("login")
        else:
            messages.error(request, "Sorry, an user with the same credentials already exits. Please login to your account")
            return redirect("login")

    else:
        return render(request, 'register.html')


def login(request):
     if request.POST:
         post_email = request.POST['email']
         post_password = request.POST['password']

         user = auth.authenticate(email=post_email,password=post_password)
         print(user)
         print(post_email)
         print(post_password)
         if user is not None:
             auth.login(request, user)


             messages.success(request, "You have been logged in.")
             return redirect('login')
         else:

             messages.error(request, "Sorry your Email/Password don't match")
             return redirect('login')



     return render(request,"login.html")

def logout(request):
    auth.logout(request)
    messages.success(request,"You have been logged out successfully")
    return redirect("home")



def account_home(request):
    pass
