from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from io import BytesIO
import zipfile, os
from .models import Product
from .models import ProductImage



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    images = product.images.all()  # related_name='images'

    return render(request, "product_detail.html", {
        "product": product,
        "images": images,
    })



def download_all_images(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()

    buffer = BytesIO()

    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for img in images:
            if img.image and os.path.exists(img.image.path):
                zipf.write(
                    img.image.path,
                    arcname=os.path.basename(img.image.path)
                )

    buffer.seek(0)

    return FileResponse(
        buffer,
        as_attachment=True,
        filename=f"{product.slug}_images.zip"
    )
