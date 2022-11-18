from django.urls import path
from apps.blog.views import blog_category_list

urlpatterns = [
    path('', blog_category_list, name='blog_category_list'),
]
