from django.shortcuts import render
from .models import Yangiliklar


def index(request):

	posts = Yangiliklar.objects.filter(status=1).order_by('-id')
	context = {'posts':posts}

	return render(request, 'index.html', context)

def detail(request, pk):
	detail = Yangiliklar.objects.get(slug=pk)
	context = {'detail':detail}
	return render(request, 'detail.html', context)
