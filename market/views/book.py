from django.http import JsonResponse
from django.shortcuts import render

from market.models.book import Book


def get_books(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        books_list.append({
            'title': book.title,
            'author_name': book.author_name,
            'price': book.price,
            'pages': book.page_count,
            'category': book.category
        })

    return JsonResponse(books_list, safe=False)


def get_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    books_list = {
        'title': book.title,
        'author_name': book.author_name,
        'price': book.price,
        'pages': book.page_count,
        'category': book.category
    }
    return JsonResponse(books_list, safe=False)
