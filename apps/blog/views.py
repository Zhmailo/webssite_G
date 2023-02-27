from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentForm
from apps.blog.models import BlogCategory, Article, Tag, Comment


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': 'Цікаві пропозції'}
    return render(request, 'blog/category/list.html', {'categories': blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    comments = Comment.objects.filter(is_checked=True)
    breadcrumbs = {reverse('blog_category_list'): "Цікаві пропозції", "current" : category.name}
    return render(
        request,
        'blog/article/list.html',
        {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs}
    )


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Цікаві пропозції',
        reverse('blog_article_list', args=[category_id]): category.name,
        'current': article.title
    }
    error = None

    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article)
        user = request.user
        if not user.is_anonymous:
            data.update(user=user, name=user.username, email=user.email, is_checked=True)
        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            breadcrumbs = {'current': 'Коментар додано'}
            return render(request, 'blog/article/created.html', {'article': article, 'breadcrumbs': breadcrumbs})
        else:
            error = form.errors

    return render(
        request,
        'blog/article/view.html',
        {'article': article, 'category': category, 'breadcrumbs': breadcrumbs, 'error': error}
    )


def tag_search_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': tag.name
    }
    return render(request,
                  'blog/tag_search.html',
                  {'tag': tag, 'articles': articles, 'breadcrumbs': breadcrumbs})