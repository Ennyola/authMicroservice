from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UploadFileForm


# Create your views here.

def signup(request):
    
    return render(request, 'registration.html')

def init_signup(request):
    first_name = request.POST.get('first_name',None)
    last_name = request.POST.get('last_name', None)
    email = request.POST.get('email', None)
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    verify_password = request.POST.get('vfpassword', None)
    if password != verify_password:
        messages.error(request, "Passwords do not match")
        return redirect("auth_app:signup")

    if User.objects.filter(email = email ).exists():
        messages.error(request, "email already exist")
        return redirect("auth_app:signup")
    elif User.objects.filter(username = username ).exists():
        messages.error(request, "username already exist")
        return redirect("auth_app:signup")
    else:
        user = User(email = email, first_name = first_name, last_name = last_name, username = username)
        user.set_password(password)
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('auth_app:homepage')
    
def login_page(request):
    return render(request, 'login.html')


def user_login(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)

    user = authenticate(username = email, password = password)
    if user:
        login(request, user)
        return redirect( "http://127.0.0.1:3000/homepage")
        "auth_app:homepage"
        
    else:
        messages.error(request, "Invalid Login Credentials")
        return redirect('auth_app:login')


def homepage(request):
    user = request.user
    if user.is_authenticated:
        pass
    else:
        return redirect('auth_app:login')
    context = {'user': user}
    return render(request, 'homepage.html', context)


def logout_view(request):
    logout(request)
    return redirect('auth_app:login')
    