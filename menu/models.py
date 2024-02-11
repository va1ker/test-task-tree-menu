from django.db import models
from django.utils.text import slugify


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
