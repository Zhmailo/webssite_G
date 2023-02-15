from rest_framework import viewsets, permissions

from apps.api.blog.serializers import ArticleSerializer
from apps.blog.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Article.objects.all()
        if self.request.query_params.get('user'):
            queryset = queryset.filter(user=self.request.query_params.get('user'))
        if self.request.query_params.get('category'):
            queryset = queryset.filter(category=self.request.query_params.get('category'))

        return queryset