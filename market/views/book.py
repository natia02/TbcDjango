from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from market.models.book import Book


def get_books(request):
    books = Book.objects.all().order_by('-id')
    paginator = Paginator(books, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'books/book_list.html', {'book': page_obj})


def get_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})
