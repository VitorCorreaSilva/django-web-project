from django.urls import path
from . import views
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from .views import ArtistListView, ArtistDetailView
from .views import ConstructionListView, ConstructionDetailView

urlpatterns = [
    path('', views.home, name='museum-home'),

    path('event', EventListView.as_view(), name='museum-event'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='museum-event-detail'),
    path('event/new/', EventCreateView.as_view(), name='museum-event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='museum-event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='museum-event-delete'),
    
    path('artist/', ArtistListView.as_view(), name='museum-artist'),
    path('artist/<int:pk>/', ArtistDetailView.as_view(), name='museum-artist-detail'),

    path('construction/', ConstructionListView.as_view(), name='museum-construction'),
    path('construction/<int:pk>/', ConstructionDetailView.as_view(), name='museum-construction-detail'),

    path('about/', views.about, name='museum-about'),
]