from django.core.management.base import BaseCommand
from categories.models import Category
from brands.models import Brand
from gallery.models import Product
from utils.slug import unique_slugify

class Command(BaseCommand):
    help = "Generate SEO-friendly unique slugs for all existing items"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("🚀 Starting SEO slug generation..."))

        # -------------------------------
        # Categories
        # -------------------------------
        for obj in Category.objects.all():
            old_slug = obj.slug
            obj.slug = unique_slugify(obj, obj.name)
            obj.save()
            self.stdout.write(f"Category: {obj.name} → {old_slug} → {obj.slug}")

        # -------------------------------
        # Brands
        # -------------------------------
        for obj in Brand.objects.all():
            old_slug = obj.slug
            obj.slug = unique_slugify(obj, obj.name)
            obj.save()
            self.stdout.write(f"Brand: {obj.name} → {old_slug} → {obj.slug}")

        # -------------------------------
        # Products
        # -------------------------------
        for obj in Product.objects.all():
            old_slug = obj.slug
            base = f"{obj.name}-{obj.brand.name if obj.brand else ''}-{obj.category.name}"
            obj.slug = unique_slugify(obj, base)
            obj.save()
            self.stdout.write(f"Product: {obj.name} → {old_slug} → {obj.slug}")

        self.stdout.write(self.style.SUCCESS("\n🎉 All slugs generated successfully!"))
