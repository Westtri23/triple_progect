from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('keys/', KeysPageView.as_view(), name='keys'),
    path('keys/<str:slug>/', KeysPageItemView.as_view(), name='keys_item'),
    path('<str:slug>', ServicesByCategory.as_view(), name='list_category'),
    path('<str:category>/<str:slug>/', ServicesPageView.as_view(), name='category'),
]
