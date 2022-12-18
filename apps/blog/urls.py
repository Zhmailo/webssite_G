from django.urls import path
from apps.blog.views import blog_category_list, article_list, article_view, tag_search_view

urlpatterns = [
    path('', blog_category_list, name='blog_category_list'),
    path('<int:category_id>/', article_list, name='blog_article_list'),
    path('tag/<int:tag_id>/', tag_search_view, name='tag_search_view'),
    path('<int:category_id>/<int:article_id>/', article_view, name='blog_article_view'),
]