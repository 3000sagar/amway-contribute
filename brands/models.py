from django.db import models
from categories.models import Category
from utils.slug import unique_slugify  # <-- import

class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = f"{self.name}"
            self.slug = unique_slugify(self, base_slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
