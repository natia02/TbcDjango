from django.urls import path
from market.views.book import get_books, get_book
from market.views.index import index
from market.views.author import get_author, get_authors
from market.views.category import get_categories, get_category

urlpatterns = [
    path('book/', get_books, name='books'),
    path('book/<int:book_id>/', get_book, name='book'),
    path('author/', get_authors, name='authors'),
    path('author/<int:author_id>/', get_author, name='author'),
    path('category/', get_categories, name='categories'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('', index, name='index')

]
