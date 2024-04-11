from django.http import JsonResponse
from market.models.book import Book


def get_books(request):
    books = Book.objects.values_list('title', 'author_name', 'price', 'page_count', 'category')
    books_list = list(books)
    return JsonResponse(books_list, safe=False)


def get_book(request, book_id):
    book = Book.objects.filter(pk=book_id).values_list('title', 'author_name', 'price', 'page_count', 'category')
    if book:
        return JsonResponse(book[0], safe=False)
    else:
        return JsonResponse({'error': 'Book not found'}, status=404)
