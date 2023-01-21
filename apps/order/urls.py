from django.urls import path
from apps.order.views import add_to_cart

urlpatterns = [
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
]