from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from market.models.category import Category


def get_categories(request):
    categories = Category.objects.all().order_by('-id')
    paginator = Paginator(categories, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'category/category_list.html', {'categories': page_obj})


def get_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = category.book_set.all()
    return render(request, 'category/category_detail.html', {'category': category, 'books': books})
