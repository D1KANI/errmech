from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user, login, logout
from django.contrib import messages
from django.core.mail import send_mail


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


class ViewItem(ListView):
    # paginate_by = 2
    model = Item
    template_name = 'item.html'
    context_object_name = 'item'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Item.objects.get(slug=self.kwargs['item_slug']).company_fk.title
        context['item'] = Item.objects.get(slug=self.kwargs['item_slug'])
        return context

    def get_queryset(self):
        return Item.objects.filter(slug=self.kwargs['item_slug'])


def register(request):
    # form = UserCreationForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = Shop.objects.create(**form.cleaned_data)
            user = form.save()
            # user = form.username
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    return render(request, 'signin.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})
