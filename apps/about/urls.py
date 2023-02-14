from django.urls import path, include
from apps.about.views import about

urlpatterns = [
    path('about', about, name='about')]