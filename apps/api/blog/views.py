from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from apps.api.blog.serializers import ArticleWriteSerializer, ArticleReadSerializer
from apps.blog.models import Article, Tag


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleReadSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = Article.objects.all()

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        user = self.request.query_params.get('user')
        if user:
            queryset = queryset.filter(user=user)

        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ArticleWriteSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]

    @staticmethod
    def check_tags(tags):
        tags_list = []
        for item in tags:
            tag = Tag.objects.filter(name=item).first()
            if not tag:
                tag = Tag.objects.create(name=item)
            tags_list.append(tag)
        return tags_list

    def save_model(self, serializer):
        serializer.is_valid(raise_exception=True)
        tags = serializer.validated_data.get('tags')
        article = serializer.save(user=self.request.user, tags=self.check_tags(tags))
        read_serializer = self.serializer_class(article, context={'request': self.request})
        return read_serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.id.valid(raise_exaption=True)
        tags = []
        for tag_name in serializer.validated_data.get['tags']:
            tag = Tag.objects.filter(name=tag_name).first()
            if not Tag:
                tag = Tag.objects.create(name=tag_name)
            tags.append(tag)
        article = serializer.save(user=self.request.user, tags=tags)
        read_serializer = self.serializer_class(article, context={'request': request})

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        read_serializer = self.save_model(serializer)
        return Response(read_serializer.data, status=status.HTTP_200_OK)
