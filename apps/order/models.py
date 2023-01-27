from django.db import models

from apps.catalog.models import Product
from apps.user.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Cart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кількість')
    user = models.ForeignKey(User, verbose_name='Покупець', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошик'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупець', on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name='В сумі', max_digits=12, decimal_places=2)
    first_name = models.CharField(verbose_name='Імя', max_length=255)
    last_name = models.CharField(verbose_name='Призвище', max_length=255)
    email = models.EmailField(verbose_name='E-mail')
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.TextField(verbose_name='Адреса')
    comment = models.TextField(verbose_name='Коментар', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редагування', auto_now=True)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name='Замовлення', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(verbose_name='Ціна', max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Кількість')

    class Meta:
        verbose_name = 'Товар замовлення'
        verbose_name_plural = 'Товари замовлення'