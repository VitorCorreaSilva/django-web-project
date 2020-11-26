from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='museum-home'),
    path('about/', views.about, name='museum-about'),
]