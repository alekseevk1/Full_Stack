from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('load/', load_more, name='load'),
    path('category/<slug:category_slug>/load/', load_more_category, name='load_cat'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('delivery/', delivery, name='delivery'),
    path('payment-orders/', payment_orders, name='payment-orders'),
    path('how-to-buy/', how_to_buy, name='how-to-buy'),
    path('products/<slug:product_slug>/', show_post, name="product"),
    path('category/<slug:category_slug>/', show_category, name="category"),
]