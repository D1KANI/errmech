from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from .models import Category, Product
from .serializers import GetCategorySerializer, GetProductsSerializer


class CategoryListApiView(ListAPIView):
    serializer_class = GetCategorySerializer
    queryset = Category.objects.all()


class CategoryCreateApiView(ListCreateAPIView):
    serializer_class = GetCategorySerializer
    queryset = Category.objects.all()


class ProductListApiView(ListAPIView):
    serializer_class = GetProductsSerializer
    queryset = Product.objects.all()


class ProductIndexListApiView(ListAPIView):
    serializer_class = GetProductsSerializer
    queryset = Product.objects.all()[:8]
