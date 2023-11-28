# example/urls.py
from django.urls import path

from .views import home, index, indexImage

urlpatterns = [
    path('', index),
    path('home/', home, name='home'),
    path('indexImage/', indexImage, name='indexImage')
]