from django.urls import path
from store.views import get_products

urlpatterns = [
    path('products/', get_products, name='get_products')
]