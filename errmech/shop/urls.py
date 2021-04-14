from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    # path('item/<int:item_id>/', NewsByCategory.as_view(), name='category'),
    path('item/<int:item_id>/', view_item, name='view_item'),
]
