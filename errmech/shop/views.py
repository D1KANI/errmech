from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.generic import *
from .models import Item


# Create your views here.
def index(request):
    return render(request, 'index.html')


def view_item(request, item_id):
    # news_item = Shop.objects.get(pk=news_id)
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item.html', {"item": item})
