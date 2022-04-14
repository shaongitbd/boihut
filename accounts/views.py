from django.shortcuts import render,redirect
from .models import AccountManager,Account
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from cart.models import Cart
# Create your views here.


def register(request):
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

            messages.error(request, 'Password and Confirm Password Does not match')
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
            user.save()
            messages.success(request, 'Your account has been registered. Please Login now')
            return redirect("login")
        else:
            messages.error(request, "Sorry, an user with the same credentials already exits. Please login to your account")
            return redirect("login")

    else:
        if request.user.is_authenticated:
            return redirect('dashboard.html')
        else:
            return render(request, 'register.html')







def login(request):
     if request.user.is_authenticated:
         return redirect("dashboard")
     if request.POST:
         session_old = request.session.session_key
         post_email = request.POST['email']
         post_password = request.POST['password']
         user = auth.authenticate(email=post_email,password=post_password)
         print(user)
         print(post_email)
         print(post_password)
         if user is not None:
             auth.login(request, user)
             session_new = request.session.session_key
             try:
               cart = Cart.objects.all().filter(cart_session=session_old)
               cart.update(cart_session = session_new)
             except:
                 pass
             messages.success(request, "You have been logged in.")
             return redirect('dashboard')
         else:
             messages.error(request, "Sorry your Email/Password don't match")
             return redirect('login')

     return render(request,"login.html")




def logout(request):
    if request.user.is_authenticated:
      auth.logout(request)
      messages.success(request,"You have been logged out successfully.")
      return redirect("home")
    else:
      messages.error(request,"Sorry you need to be logged in to do this action")
      return redirect("login")



def account_home(request):
    if request.user.is_authenticated:
        context={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        return render(request, "dashboard.html",context=context)
    else:
         messages.error(request,"Sorry, You are not logged in. Please Login and try again")
         return redirect("login")




def profile_edit(request):
    if request.user.is_authenticated:
        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            user = Account.objects.all().filter(username=request.user.username)
            user.update(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone=phone)
            messages.success(request, "Your Profile has been updated")

        return render(request, "dashboard.html")
    else:
        messages.error(request,"Sorry, You need to be logged in to do this action.")
        return redirect('login')

