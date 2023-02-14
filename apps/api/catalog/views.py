from rest_framework import generics, permissions, viewsets
from apps.catalog.models import Category, Product
from apps.api.catalog.serializers import CategorySerializer, ProductReadSerializer, ProductWriteSerializer, \
    ProductImageSerializer, ProductImage


class ProductListView(generics.ListAPIView):
    serializer_class = ProductReadSerializer

    # queryset = Product.objects.filter(is_checked=True)

    def get_queryset(self):
        queryset = Product.objects.filter(is_checked=True)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(categories=category)

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=category)

        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ProductDeleteVeiw(generics.DestroyAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]


class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]
