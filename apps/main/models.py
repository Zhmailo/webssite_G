from django.db import models
from tinymce.models import HTMLField

from apps.catalog.models import Product
from apps.main.mixins import MetaTagMixin


class Page(MetaTagMixin):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Зміст', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Інформаційна сторінка'
        verbose_name_plural = 'Інформаційні сторінки'


class ProductSet(models.Model):
    products = models.ManyToManyField(Product, verbose_name='Продукти')
    name = models.CharField(verbose_name='Назва', max_length=255)
    sort = models.PositiveIntegerField(verbose_name='Сортування', default=0)
    is_active = models.BooleanField(verbose_name='Активовано', default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort']
        verbose_name = 'Карусель товару'
        verbose_name_plural = 'Карусель товарів'
