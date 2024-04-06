from django.contrib import admin
from market.models.book import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'price']
    search_fields = ['title', 'author_name']
    list_filter = ['price', 'author_name']