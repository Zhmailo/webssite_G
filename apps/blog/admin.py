from django.contrib import admin
from apps.blog.models import BlogCategory, Article, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


admin.site.register(Tag)

@admin.register(BlogCategory)
class BlogCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_count']
    list_display_links = ['id', 'name']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']

    def article_count(self, instance):
        articles = Article.objects.filter(category=instance).count()
        url = reverse('admin:blog_article_changelist') + '?' + urlencode({'category__id__exact': instance.id})
        return format_html(f"<a href='{url}'>Статей: {articles}</a>")

    article_count.short_description = 'Статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category_link', 'tag_link', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['category', 'tags']

    def category_link(self, instance):
        url = reverse('admin:blog_blogcategory_change', args=[instance.category_id])
        return format_html(f"<a href='{url}'>{instance.category.name}</a>")

    category_link.short_description = 'Категория'

    def tag_link(self, instance):
        str_end = f""
        for tag in instance.tags.all():
            url = reverse('admin:blog_tag_change', args=[tag.id])
            str_end += f"<a href='{url}'>#{tag.name}, </a>"
        str_end = str_end[: str_end.rfind(",")]
        return format_html(str_end)

    tag_link.short_description = 'Теги'