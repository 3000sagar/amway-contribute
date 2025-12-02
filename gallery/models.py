from django.db import models
from categories.models import Category
from brands.models import Brand
from django.utils.text import slugify
from categories.models import Category
from brands.models import Brand
from utils.slug import unique_slugify

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)
    brand = models.ForeignKey("brands.Brand", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="products/", blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = f"{self.name}-{self.brand.name if self.brand else ''}-{self.category.name}"
            self.slug = unique_slugify(self, base_slug)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
