from django.urls import path, include
from apps.more.views import more

urlpatterns = [
    path('more', more, name='more')]