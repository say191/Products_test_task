from django.urls import path
from .views import ProductListCreateView, index

urlpatterns = [
    path('', index, name='index'),
    path('products/', ProductListCreateView.as_view(), name='product_list'),
]
