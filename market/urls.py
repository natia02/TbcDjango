from django.urls import path
from market.views.book import get_books, get_book
from market.views.index import index

urlpatterns = [
    path('books/', get_books, name='books'),
    path('books/<int:book_id>/', get_book, name='book'),
    path('', index, name='index')

]
