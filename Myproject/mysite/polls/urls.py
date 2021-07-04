from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('Bai1', views.Bai1, name='Bai1'),
    path('Bai2', views.Bai2, name='bai2'),
    path('Bai3', views.Bai3, name='bai3'),
]
