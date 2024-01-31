from django.contrib import admin

from shop.forms import ProductAdminForm
from shop.models import Category, Product


# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    readonly_fields = ("slug",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    readonly_fields = ("created_at", "updated_at", "slug")
