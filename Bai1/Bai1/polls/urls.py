from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.base, name='base'),
]