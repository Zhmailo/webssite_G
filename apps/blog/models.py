from django.db import models


# Create your models hear.


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категория блога'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory, verbose_name='Категории', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
