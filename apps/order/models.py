from django.db import models

from apps.catalog.models import Product
from apps.user.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Кількість")
    user = models.ForeignKey(User, verbose_name="Покупець", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошики'
