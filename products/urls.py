from django.urls import path
from .views import create_product, get_all_product


urlpatterns = [
    path('product',create_product),
    path('products',get_all_product)
]