from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.generic import *
from .models import *


# Create your views here.
class Home(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['news'] = News.objects.order_by('created_at')[:4]
        return context

    def get_queryset(self):
        return Item.objects.order_by('-views')[:8]


class CategoriesList(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Категории'}


class NewsList(ListView):
    model = News
    template_name = 'articles.html'
    context_object_name = 'news'
    extra_context = {'title': 'Статьи'}
    ordering = '-created_at'


def view_item(request):
    return render(request, 'item.html')
