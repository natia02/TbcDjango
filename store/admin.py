from django.contrib import admin
from store.models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity")
    search_fields = ("name", "price")
    list_filter = ("price", "quantity")
