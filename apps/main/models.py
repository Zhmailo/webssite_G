from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from apps.main.mixins import MetaTagMixin


class Page(MetaTagMixin):
    name = models.CharField(verbose_name='Назван', max_length=128)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Опис', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Інформаційна сторінка'
        verbose_name_plural = 'Інформаційні сторінки'


