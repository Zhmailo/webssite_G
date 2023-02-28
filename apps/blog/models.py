from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from apps.main.mixins import MetaTagMixin
from apps.user.models import User
from config.settings import MEDIA_ROOT


class BlogCategory(MetaTagMixin):
    name = models.CharField(verbose_name="Ім'я категорії", max_length=255)
    # image = models.ImageField(verbose_name='Картинка', upload_to='blog/categoty/', null=True)
    image = ProcessedImageField(
        verbose_name='Картинка',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія блога'
        verbose_name_plural = 'Категорії блога'

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Картинка'

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Наявна картинка'


class Tag(MetaTagMixin):
    name = models.CharField(verbose_name="Напишіть тег", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(MetaTagMixin):
    category = models.ForeignKey(to=BlogCategory, verbose_name='Категорія', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name="Текст-прев'ю", null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    tag = models.ManyToManyField(to=Tag, verbose_name='Теги', blank=True)
    image = ProcessedImageField(
        verbose_name='Картинка',
        upload_to='blog/category/',
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    publish_date = models.DateTimeField(verbose_name='Дата публікації')
    updated_at = models.DateTimeField(verbose_name='Дата зміни', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'


class Comments(models.Model):
    user = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name="Ваше ім'я", null=True, blank=True, max_length=255)
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    article = models.ForeignKey(to=Article, verbose_name='Стаття', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    is_active = models.BooleanField(verbose_name='Активовано', default=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарій'
        verbose_name_plural = 'Коментарі'
