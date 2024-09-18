from django.db import models


class Product(models.Model):
    """
    Модель продукта, которая включает в себя набор полей, таких как:
    назваоние, описание и цена
    """

    name = models.CharField(max_length=30, verbose_name='name')
    description = models.TextField(max_length=500, verbose_name='description')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
