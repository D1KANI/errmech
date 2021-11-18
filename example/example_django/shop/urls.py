from django.urls import path, include
from shop import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view(), name="latest_product")
]