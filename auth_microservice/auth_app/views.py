from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User



# Create your views here.

def signup(request):
    
    return render(request, 'registration.html')


def login_page(request):
    return render(request, 'login.html')


def homepage(request):

    return render(request, 'homepage.html')


    