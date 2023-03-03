from django.contrib import admin
from apps.blog.models import BlogCategory, Article, Tag, Comments
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_count']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']

    def article_count(self, instance):
        articles = Article.objects.filter(category=instance).count()
        url = reverse('admin:blog_article_changelist') + '?' + urlencode({'category__id__exact': instance.id})
        return format_html(f'<a href="{url}">Статей: {articles}</a>')

    article_count.short_description = 'Кількість статей'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category_link', 'user_link', 'tag_list', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['category', 'tag']

    def category_link(self, instance):
        url = reverse('admin:blog_blogcategory_change', args=[instance.category_id])
        return format_html(f"<a href='{url}'>{instance.category.name}</a>")

    category_link.short_description = 'Категорії'

    def user_link(self, instance):
        if instance.user:
            url = reverse('admin:user_user_change', args=[instance.user.id])
            return format_html(f"<a href='{url}'>{instance.user}</a>")

    user_link.short_description = 'Автор'

    def tag_list(self, instance):
        tags = instance.tag.all()
        # string_html = ''
        # for i in range(len(tags)):
        #     if i != 0:
        #         string_html += ', '
        #     string_html += f"<a href='{reverse('admin:blog_tag_change', args=[tags[i].id])}'>{tags[i].name}</a>"
        # if tags:
        #     return format_html(string_html)

        data = []
        for tag in tags:
            url = reverse('admin:blog_tag_change', args=[tag.id])
            data.append(f"<a href='{url}'>{tag.name}</a>")
        # data = str(data)[1:-1]
        result = ', '.join(data)
        return format_html(result)

    tag_list.short_description = 'Теги'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'article', 'created_at']
    list_display_links = ['id', 'name']
