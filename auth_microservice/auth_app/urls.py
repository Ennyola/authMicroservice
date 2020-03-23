from django.contrib import admin
from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('login/', views.login_page, name = 'login'),
    path('login_user/', views.user_login, name = 'user_login' ),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.init_signup, name = "signin"),
    path('homepage/', views.homepage, name = "homepage"),
    path('logout/', views.logout_view, name = "logout")
]