from django.urls import path

from .views import *

urlpatterns = [
    path('', contactView, name='home_form'),
]
