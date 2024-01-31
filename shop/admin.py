from django.contrib import admin

from shop.models import Category


# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    readonly_fields = ("slug",)
