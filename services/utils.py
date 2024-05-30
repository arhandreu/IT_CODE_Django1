from uuid import uuid4
from django.utils.text import slugify


def unique_slugify(instance, slug):

    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug
