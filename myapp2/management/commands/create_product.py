from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):

        for i in range(1, 6):
            product = Product(
                product_name=f"product{i}",
                description=f"description{i}",
                price=i * 1.1,
                count_product=i,
            )
            product.save()
        self.stdout.write(self.style.SUCCESS("Some fake products are registered"))
