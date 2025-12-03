from django.shortcuts import render, get_object_or_404
from .models import Category
from brands.models import Brand
from gallery.models import Product, ProductImage
from django.db.models import Q

# HOME PAGE
def category_list(request):
    categories = Category.objects.all()
    featured = Product.objects.all()[:6]

    random_images = (
        ProductImage.objects
        .select_related("product")
        .order_by("?")[:20]
    )

    slides = [
        {
            "title": "Nutrition For<br>Daily Strength",
            "subtitle": "Premium supplements for everyday wellness.",
            "image": "/media/category_images/Nutrition_375x280.png",
            "gradient_from": "#4F46E5",
            "gradient_to": "#2563EB",
        },
        {
            "title": "Beauty That<br>Glows",
            "subtitle": "Artistry & Attitude special care.",
            "image": "/media/category_images/Beauty_375x280.png",
            "gradient_from": "#DB2777",
            "gradient_to": "#F87171",
        },
        {
            "title": "Personal Care<br>For Everyone",
            "subtitle": "Glister, Satinique, G&H essentials.",
            "image": "/media/category_images/personal_care1_fixed.png",
            "gradient_from": "#1D4ED8",
            "gradient_to": "#06B6D4",
        },
    ]

    return render(request, 'category_list.html', {
        "categories": categories,
        "featured": featured,
        "random_images": random_images,
        "slides": slides,
    })

def first_image_url(product):
    """Return first related image or fallback product.image."""
    img = product.images.first()
    if img:
        try:
            return img.image.url
        except:
            pass

    if product.image:
        try:
            return product.image.url
        except:
            pass

    return None


def search(request):
    query = (request.GET.get("q") or "").strip()

    results = []

    if query:
        qs = Product.objects.filter(
            Q(name__icontains=query) |
            Q(slug__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(brand__name__icontains=query)
        ).distinct()

        for p in qs:
            results.append({
                "obj": p,
                "name": p.name,
                "snippet": (p.description[:150] + "...") if p.description else "",
                "image": first_image_url(p),
            })

    return render(request, "search.html", {
        "query": query,
        "results": results,
    })
def all_products(request):
    products = Product.objects.all().order_by("name")
    return render(request, "all_products.html", {"products": products})

def contact_page(request):
    return render(request, "contact.html")

# CATEGORY DETAIL PAGE
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    other_categories = Category.objects.exclude(id=category.id)

    brand_id = request.GET.get("brand")
    brands = Brand.objects.filter(category=category)

    products = Product.objects.filter(category=category)

    if brand_id:
        products = products.filter(brand_id=brand_id)

    return render(request, "category_detail.html", {
        "category": category,
        "products": products,
        "brands": brands,
        "selected_brand": brand_id,
        "other_categories": other_categories,
    })

