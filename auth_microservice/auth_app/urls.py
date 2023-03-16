from django.contrib import admin
from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('login/', views.login_page, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('homepage/', views.homepage, name = "homepage"),
]