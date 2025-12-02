from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    # PRODUCT DETAIL: /product/<slug>/
    path("<slug:slug>/", views.product_detail, name="product_detail"),

    # DOWNLOAD ALL IMAGES: /product/<slug>/download-all/
    path("<slug:slug>/download-all/", views.download_all_images, name="download_all"),
]
