from django.contrib import admin
from django.urls import path
from API.views import *

urlpatterns = [
    path('', SaveData.as_view(http_method_names=['post'])),
    path('get-data/', SaveData.as_view(http_method_names=['get'])),
]
