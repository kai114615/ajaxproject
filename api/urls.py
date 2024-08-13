from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('cities/', views.cities),

    # http://127.0.0.1:8000/api/districts/縣市名
    path('districts/<str:city_name>', views.districts)
]
