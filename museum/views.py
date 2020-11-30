from django.shortcuts import render
from .models import Construction, Event, Artist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
	context = {
		'constructions': Construction.objects.all()
	}
	return render(request, 'museum/home.html', context)

def construction(request):
	context = {
		'constructions': Construction.objects.all()
	}
	return render(request, 'museum/construction.html', context)

def artist(request):
	context = {
		'artists': Artist.objects.all()
	}
	return render(request, 'museum/artist.html', context)

def about(request):
	return render(request, 'museum/about.html', {'title':'about'})



def event(request):
	context = {
		'events': Event.objects.all()
	}
	return render(request, 'museum/event.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'museum/event.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['-date_created']


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'event_date', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False