from django.contrib import admin
from django.urls import path, include,re_path
from book_app import views

# from django.conf.urls import url, include

urlpatterns = [
    path(r'index/', views.index),
    re_path(r'(\d+)/', views.detail),
]
