from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login),
    path('update-metadata', views.updateMetadata),
    path('send-cookie', views.getCookie),
]
