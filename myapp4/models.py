from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone:{self.phone}, address:{self.address}'
