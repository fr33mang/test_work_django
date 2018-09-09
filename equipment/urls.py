from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_vehicles', views.get_vehicles, name='get_vehicles'),
]