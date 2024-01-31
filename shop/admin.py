from django.contrib import admin

from shop.forms import ProductAdminForm
from shop.models import Category, Product, MainCategory


# Register your models here.


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    readonly_fields = ("created_at", "updated_at", "slug")
    list_display = ("title", "price", "count", "condition", "category", "created_at", "updated_at")
    list_filter = ("condition", "count", "category", "created_at", "updated_at")
    search_fields = ("title",)
