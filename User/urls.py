
from django.urls import path

from . import views

urlpatterns = [
    path('', views.register),
    path('activate/', views.activate),
]