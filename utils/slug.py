from django.utils.text import slugify

def unique_slugify(instance, base, slug_field="slug"):
    slug = slugify(base)
    slug = f"amway-{slug}"   # Add 'amway' prefix globally

    ModelClass = instance.__class__
    counter = 1
    unique_slug = slug

    while ModelClass.objects.filter(**{slug_field: unique_slug}).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1

    return unique_slug
