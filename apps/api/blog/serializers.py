from rest_framework import serializers

from apps.blog.models import Article, BlogCategory, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class BlogCategorySerializer(serializers.ModelSerializer):  #
    class Meta:
        model = BlogCategory
        fields = ('id', 'name', 'image')


class ArticleWriteSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=64))  #

    class Meta:
        model = Article
        fields = (
            'id',
            'images',
            'category',
            'user',
            'image',
            'title',
            'text_preview',
            'text',
            'publish_date',
            'tags'
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'images',
            'product',
            'is_main'
        )


class ArticleReadSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    tags = TagSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'category',
            'user',
            'image',
            'images',
            'main_image',
            'title',
            'text_preview',
            'text',
            'publish_date',
            # 'image_thumbnail',
            'created_at',
            'tags'
        )
