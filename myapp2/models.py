from decimal import Decimal

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    date_create = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'Username: {self.name}, '
                f'email: {self.email}, '
                f'phone:{self.phone}'
                f'address:{self.address}'
                f'date_create:{self.date_create}'
                )


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_create = models.DateField(auto_now_add=True, null=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)
    image_product = models.ImageField(null=True)

    def __str__(self):
        return (f'product_name: {self.product_name}, '
                f'description: {self.description}, '
                f'price:{self.price}'
                f'count_product:{self.quantity}'
                f'date_create:{self.date_create}'
                f'rating:{self.rating}'
                )


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    date_ordered = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'customer: {self.customer}, '
                f'products: {self.products}, '
                f'total_price:{self.total_price}'
                f'date_ordered:{self.date_ordered}'
                )

    def calculate_total(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_price = total
        self.save()



