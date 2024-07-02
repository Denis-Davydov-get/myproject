from django.contrib import admin
from django.urls import path, include
from .views import all_product, add_product

urlpatterns = [
    path('products/', all_product, name='all_product'),
    path("add_product/", add_product, name="add_product"),  # адрес для создания нового товара
]
