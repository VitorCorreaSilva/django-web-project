from django.shortcuts import render
from .models import Construction


def home(request):
	context = {
		'constructions': Construction.objects.all()
	}
	return render(request, 'museum/home.html', context)

def about(request):
	return render(request, 'museum/about.html', {'title':'about'})