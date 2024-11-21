from django.urls import path
from .views import fetch_and_save_cities

urlpatterns = [
    path('fetch-cities/', fetch_and_save_cities, name='fetch_cities'),
]
