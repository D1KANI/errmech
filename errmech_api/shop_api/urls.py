from .views import CategoryListApiView, CategoryCreateApiView, ProductListApiView, ProductIndexListApiView
from django.urls import path

urlpatterns = [
    path('getcategories/', CategoryListApiView.as_view()),
    path('getproducts/', ProductListApiView.as_view()),
    path('getproductsforindex/', ProductIndexListApiView.as_view()),
    path('createcategories/', CategoryCreateApiView.as_view()),
]
