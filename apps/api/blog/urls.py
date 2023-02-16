from apps.api.blog.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView,\
    ArticleUpdateView, ArticleListView
from django.urls import path


urlpatterns = [
    path('article/', ArticleListView.as_view()),
    path('article/<int:pk>/', ArticleDetailView.as_view()),
    path('article/create/', ArticleCreateView.as_view()),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view()),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view()),
]