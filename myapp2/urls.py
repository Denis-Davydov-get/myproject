from django.urls import path
from .views import orders, index

urlpatterns = [
    path('orders/', orders, name='orders'),
    path('orders/<int:client_id>', orders, name='orders'),
    path('', index, name='index'),

]
