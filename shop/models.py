from django.db import models
from transliterate import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, "ru")
        super().save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
