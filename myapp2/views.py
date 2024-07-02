import logging
from datetime import timedelta, datetime

from django.shortcuts import render, get_object_or_404
from myapp2.models import Order, User

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "myapp2/index.html", {"title": "Homepage"})


def orders(request, client_id: int = None):
    if client_id:
        client = get_object_or_404(User, id=client_id)
        order = Order.objects.filter(customer=client)
        today = datetime.today()

        # Заказы клиента за период времени
        order_week = order.filter(date_ordered__gte=today - timedelta(days=7))
        order_month = order.filter(date_ordered__gte=today - timedelta(days=30))
        order_year = order.filter(date_ordered__gte=today - timedelta(days=365))

        # Получаем уникальные продукты в заказах
        products_week = {product for order in order_week for product in order.products.all()}
        products_month = {product for order in order_month for product in order.products.all()}
        products_year = {product for order in order_year for product in order.products.all()}

        context = {
            "title": f"Список заказов клиента {client.name}",
            "client": client,
            "order": order,
            "products_week": products_week,
            "products_month": products_month,
            "products_year": products_year,
        }
    else:
        order = Order.objects.all()
        context = {"title": f"Список всех заказов", "order": order}
    return render(request, "myapp2/orders.html", context)
