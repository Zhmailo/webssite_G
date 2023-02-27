from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from apps.user.models import User
from config.settings import MEDIA_ROOT
from apps.main.mixins import MetaTagMixin


class BlogCategory(MetaTagMixin):
    name = models.CharField(verbose_name='Назва категорії', max_length=255)
    # image = models.ImageField(verbose_name='Изабражение', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Зображення'

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Зображення'


class Tag(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тегі'


class Article(MetaTagMixin):
    category = models.ForeignKey(to=BlogCategory, verbose_name='Пропозиція', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью', null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикації')
    tags = models.ManyToManyField(to=Tag, verbose_name='Теги', blank=True)
    image = ProcessedImageField(
        verbose_name='Зображення',
        upload_to='blog/article/',
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    updated_at = models.DateTimeField(verbose_name='Дата зміни', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.title

    class Meta:
        verbose_name = 'Пропозиція'
        verbose_name_plural = 'Пропозиції'


class Comment(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='Статья')
    user = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name="Ваше ім'я", null=True, blank=True, max_length=255)
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Коментар')
    is_checked = models.BooleanField(verbose_name='Перевірено', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
