from django.contrib import admin
from market.models.book import Book
from market.models.author import Author
from market.models.category import Category


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'page_count', 'price']
    search_fields = ['title']
    list_filter = ['price', 'page_count']
