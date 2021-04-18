from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', Home.as_view(), name="home"),
    path('category/', CategoriesList.as_view(), name="categories"),
    path('news/', NewsList.as_view(), name="news"),
    # path('item/<int:item_id>/', NewsByCategory.as_view(), name='category'),
    path('item/<slug:item_slug>/', ViewItem.as_view(), name='item'),
]
