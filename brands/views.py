from django.shortcuts import render, get_object_or_404
from .models import Brand
from gallery.models import Product


def product_list(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    products = Product.objects.filter(brand=brand)

    return render(request, "all_products.html", {
        "brand": brand,
        "products": products,
    })
