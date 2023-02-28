from django.shortcuts import render
from django.urls import reverse
from django.db import transaction

from apps.blog.models import BlogCategory, Article, Tag, Comments
from apps.blog.forms import CreateCommentForm


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': 'Блог'}

    return render(
        request,
        'blog/category_list.html',
        {"categories": blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': category.name
    }

    return render(
        request,
        'blog/article_list.html',
        {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    comment = Comments.objects.filter(article=article, is_active=True)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        reverse('blog_article_list', args=[category_id]): category.name,
        'current': article.title
    }

    error = None
    user = request.user
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article)
        if not user.is_authenticated:
            data.update(is_active=False)
        else:
            data.update({"name": f"{user.last_name} {user.first_name}", "is_checked": True,
                         "email": user.email, "user": user})
            request.POST = data
            form = CreateCommentForm(request.POST)
            if form.is_valid():
                try:
                    with transaction.atomic():
                        comment = form.save()
                        breadcrumbs = {'current': 'Коментар створено'}
                        return render(request, 'blog/created_comment.html',
                                      {'breadcrumbs': breadcrumbs, 'category_id': article.category.id,
                                       'article_id': article.id})
                except Exception as e:
                    error = f'Коментарій не створився. {e}. Напишіть будь ласка нашому менеджеру'

            else:
                error = form.errors
        if user.is_authenticated:
            form = CreateCommentForm(data={
                'name': user.first_name,
                'email': user.email
            })
        else:
            form = CreateCommentForm()

    comments = Comments.objects.filter(is_active=True, article=article)
    return render(
        request,
        'blog/article_view.html',
        {'article': article, 'category': category, 'comments': comments, 'form': form, 'error': error,
         'breadcrumbs': breadcrumbs})


def tag_article(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tag=tag_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': tag.name
    }
    return render(request,
                  'blog/tag_article.html',
                  {'tag': tag, 'articles': articles, 'breadcrumbs': breadcrumbs})


def create_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article_id)

        if not request.user.is_anonymous:
            user = request.user
            data.update(
                {"name": f"{user.last_name} {user.first_name}", "is_active": True, "email": user.email, "user": user})

        request.POST = data
        form = CreateCommentForm()
        if form.is_valid():
            comment = form.save()
            breadcrumbs = {"current": "Коментар додано"}
            return render(request, 'blog/comment_created.html',
                          {"comment": comment, "breadcrumbs": breadcrumbs, "article": article})
