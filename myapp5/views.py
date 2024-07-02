from django.shortcuts import render

from myapp2.models import User


def all_user(request):
    users = User.objects.all()
    return render(request, 'myapp5/users.html', {"users": users})
