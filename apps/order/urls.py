from django.urls import path
from apps.order.views import add_to_cart, cart_view

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart_view/', cart_view, name='cart_view'),#####
]