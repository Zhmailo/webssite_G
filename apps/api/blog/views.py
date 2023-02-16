from rest_framework import generics, permissions
from apps.api.blog.serializers import ArticleSerializer
from apps.blog.models import Article


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        user = self.request.query_params.get('user')
        if user:
            queryset = queryset.filter(user=user)

        return queryset


class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleUpdateView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ArticleDeleteView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAdminUser]
