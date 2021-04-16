from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/', CategoriesList.as_view(), name="categories"),
    path('news/', NewsList.as_view(), name="news"),
    # path('item/<int:item_id>/', NewsByCategory.as_view(), name='category'),
    path('items/', view_item, name='view_item'),
]
