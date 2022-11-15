from django.contrib import admin
from apps.blog.models import BlogCategory, Article


admin.site.register(BlogCategory)
admin.site.register(Article)
