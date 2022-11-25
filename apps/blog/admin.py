from django.contrib import admin
from apps.blog.models import BlogCategory,Article,Tag


admin.site.register(BlogCategory)
admin.site.register(Article)
admin.site.register(Tag)