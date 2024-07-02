import logging
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageForm
from myapp2.models import Product

logger = logging.getLogger(__name__)


def all_product(request):
    products = Product.objects.all()
    return render(request, 'myapp4/products.html', {"products": products})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                product_name=form.cleaned_data["product_name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                quantity=form.cleaned_data["quantity"],
                image_product=form.cleaned_data["image_product"],
            )
            product.save()
            return redirect(all_product)
    else:
        form = ProductForm()
    context = {"title": "Добавить товар", "form": form}
    return render(request, "myapp4/new_product.html", context)
