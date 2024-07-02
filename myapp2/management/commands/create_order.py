import random

from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            client = User.objects.get(id=i)
            list_products = [Product.objects.get(id=random.randint(1,5)) for _ in range(3)]
            order = Order.objects.create(customer=client)
            order.products.add(*list_products)
            order.calculate_total()
            order.save()

        self.stdout.write(self.style.SUCCESS("Fake orders is added"))
