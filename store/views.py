from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product


# Create your views here.

def get_products(request):
    products = Product.objects.all()
    products_as_list = []

    for product in products:
        products_as_list.append({
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'description': product.description
        })

    return HttpResponse(products_as_list)
