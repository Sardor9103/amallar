from django.urls import path
from .views import amallar

urlpatterns=[
    path('',amallar,name='amallar')
]