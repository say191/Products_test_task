from rest_framework.viewsets import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Контроллер для создания нового продукта и просмотра списка продуктов.
    При обработкt GET запроса, будет отображаться список продуктов,
    при обработке POST запроса, будет создаваться новый продукт с введенными параметрами запроса
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request):
    """
    Функция для обработки HTTP запроса, передавая его в шаблон index.html для рендеринга,
    в результате чего отображает главную страницу приложения
    """
    return render(request, 'index.html')
