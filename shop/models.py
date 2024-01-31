from django.db import models
from transliterate import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, "ru")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    CONDITION_CHOICES = {"NEW": "Новый", "USED": "Б/У"}

    title = models.CharField(max_length=100, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, null=True, verbose_name="Фотография")
    count = models.PositiveIntegerField(default=0, verbose_name="Количество товара")
    category = models.ForeignKey(Category, related_name="products", on_delete=models.PROTECT, verbose_name="Категория")
    condition = models.CharField(max_length=100, unique=True, choices=CONDITION_CHOICES, verbose_name="Состояние")
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, "ru")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
