from django.contrib import admin
from django.urls import path
from market.views.book import get_books, get_book

urlpatterns = [
    path('books/', get_books, name='books'),
    path('books/<int:book_id>/', get_book, name='book')
]