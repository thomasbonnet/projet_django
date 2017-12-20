from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liste/', views.liste, name='liste'),
]