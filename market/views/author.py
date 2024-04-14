from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from market.models.author import Author


def get_authors(request):
    authors = Author.objects.all().order_by('-id')
    paginator = Paginator(authors, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'author/author_list.html', {'authors': page_obj})


def get_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = author.book_set.all()
    return render(request, 'author/author_detail.html', {'author': author, 'books': books})
