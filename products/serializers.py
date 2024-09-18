from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели продукта
    """

    class Meta:
        model = Product
        fields = '__all__'
        
    def validate_price(self, value):
        """
        Валидация значения цены продукта на уровне сериализации данных,
        для избежания возможности ввода отрицательного значения
        """
        if value <= 0:
            raise serializers.ValidationError('The price must be a positive number')
        return value

    def validate_name(self, value):
        """
        Валидация значения названия продукта на уровне сериализации данных,
        для избежания возможности ввода пустой строки
        """

        if not value.strip():
            raise serializers.ValidationError("The title can't be empty")
        return value
