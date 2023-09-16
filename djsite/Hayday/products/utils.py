from .models import *


menu = [{'title' : "О магазине", 'url_name': 'about'},
        {'title' : "Доставка", 'url_name': 'delivery'},
        {'title' : "Оплата заказов", 'url_name': 'payment-orders'},
        {'title' : "Как купить", 'url_name': 'how-to-buy'},
        {'title' : "Контакты", 'url_name': 'contacts'}]

class DataMixin:


    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['category'] = cats
        return context
