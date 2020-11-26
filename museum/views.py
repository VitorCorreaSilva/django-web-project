from django.shortcuts import render
from django.http import HttpResponse

constructions = [
	{
		'name':'Monalisa',
		'author':'Leonardo da Vinci',
		'creation_date':'August 27, 1513'
	},
	{
		'name':'O Grito',
		'author':'Edvard Munch',
		'creation_date':'August 27, 1893'
	}
]


def home(request):
	context = {
		'constructions': constructions
	}
	return render(request, 'museum/home.html', context)

def about(request):
	return render(request, 'museum/about.html', {'title':'about'})