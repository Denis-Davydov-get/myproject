from django.contrib import admin
from django.urls import path, include
from .views import all_user

urlpatterns = [
    path('users/', all_user, name='all_user'),
]
