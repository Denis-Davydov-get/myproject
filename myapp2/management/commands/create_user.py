from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            user = User(
                name=f"Client {i}",
                email=f"example{i}@mail.com",
                phone=7222-33-33 + i,
                address="Spb",
            )
            user.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{user}' is registered"))
