from rest_framework import generics, permissions, viewsets
from apps.catalog.models import Category, Product, ProductImage
from apps.api.catalog.serializers import CategorySerializer, ProductReadSerializer, ProductWriteSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductReadSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ProductDeleteVeiw(generics.DestroyAPIView):
    serializer_class = ProductWriteSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
