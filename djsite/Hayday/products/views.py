from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .utils import *
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

menu = [{'title' : "О магазине", 'url_name': 'about'},
        {'title' : "Доставка", 'url_name': 'delivery'},
        {'title' : "Оплата заказов", 'url_name': 'payment-orders'},
        {'title' : "Как купить", 'url_name': 'how-to-buy'},
        {'title' : "Контакты", 'url_name': 'contacts'}]

start_offset = 3

def index(request):
    products = Products.objects.filter(action=True)[0:start_offset]
    # post_values = Post.objects.values()[0:5]
    # print(post_values)
    total_obj = Products.objects.filter(action=True).count()
    
    context = {
        'products': products,
        'menu': menu,
        'title': 'Главная страница',
        'total_obj': total_obj,
        'action_active': True,
    }

    return render(request, 'products/index.html', context=context)


def load_more(request):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    post_obj = list(Products.objects.filter(action=True).values()[offset_int + start_offset:offset_int+start_offset
                                                             +limit])
    data = {
        'products': post_obj,
        'action_active': True,
    }
    return JsonResponse(data=data)


"""class ProductsHome(DataMixin, ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))"""

def about(request):
    return render(request, 'products/about.html', {'title': 'О Магазине', 'menu':  menu})

def cats(request, cat_id):
    return HttpResponse(f"<h1>Статьи про Магазин</h1><br><p>{cat_id}</p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Хрен знает че ты хош</h1>')

def contacts(request):
    return render(request, 'products/contacts.html', {'title': 'Контакты', 'menu':  menu})

def delivery(request):
    return render(request, 'products/delivery.html', {'title': 'Доставка', 'menu':  menu})

def payment_orders(request):
    return render(request, 'products/payment-orders.html', {'title': 'Оплата заказов', 'menu':  menu})

def how_to_buy(request):
    return render(request, 'products/how-to-buy.html', {'title': 'Как купить', 'menu':  menu})


"""class ShowProduct(DataMixin, DetailView):
    model = Products
    template_name = 'products/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))


class ProductsCategory(DataMixin, ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Products.objects.filter(category__slug=self.kwargs['category_slug'], is_Ready=True)
    
    def get_context_data(self, *, object_list=None, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['products'][0].category))
        return dict(list(context.items()) + list(c_def.items()))
    

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'products/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))"""
    
def show_post(request, product_slug):
    products = get_object_or_404(Products, slug=product_slug)

    context = {
        'products': products,
        'menu': menu,
        'title': products.title,
        'action_active': False,
    }

    return render(request, 'products/product.html', context=context)

def show_category(request, category_slug):
    products = Products.objects.filter(category__slug=category_slug)[0:start_offset]
    print(products)

    total_obj = Products.objects.filter(category__slug=category_slug).count()
    print(total_obj)

    if len(products) == 0:
        raise Http404()

    context = {
        'products': products,
        'menu': menu,
        'title': 'Отображение по категориям',
        'action_active': False,
        'total_obj': total_obj,
    }

    return render(request, 'products/index.html', context=context)

def load_more_category(request, category_slug):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    post_obj = list(Products.objects.filter(category__slug=category_slug).values()[offset_int + start_offset:offset_int+start_offset
                                                             +limit])
    print(post_obj)
    data = {
        'products': post_obj,
        'action_active': False,
    }
    return JsonResponse(data=data)