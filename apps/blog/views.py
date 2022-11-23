from django.shortcuts import render
from apps.blog.models import BlogCategory, Article


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category_list.html', {'categories': blog_categories})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    return render(request, 'blog/article_list.html', {'articles': articles, 'category': category})


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/article_view.html', {'category': category, 'article': article})
