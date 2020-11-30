from django.urls import path
from . import views
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView
)

urlpatterns = [
    path('', views.home, name='museum-home'),

    path('event', EventListView.as_view(), name='museum-event'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='museum-event-detail'),
    path('event/new/', EventCreateView.as_view(), name='museum-event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='museum-event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='museum-event-delete'),
 
    path('about/', views.about, name='museum-about'),
    path('construction/', views.construction, name='museum-construction'),
    path('artist/', views.artist, name='museum-artist'),
]