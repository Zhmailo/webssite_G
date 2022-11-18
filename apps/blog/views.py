from django.shortcuts import render
from apps.blog.models import BlogCategory


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category_list.html', {"categories": blog_categories})
