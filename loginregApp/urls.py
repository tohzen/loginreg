from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("success", views.home),
    path("logout", views.logout),
    path("login", views.login),
    
]
