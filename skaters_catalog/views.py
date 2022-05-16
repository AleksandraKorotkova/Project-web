from django.shortcuts import render
from .models import skater, trainer, element
from django.views import generic
#from django.views.generic import ListView
#from django.views.generic import DetailView

def index(request):
	
	return render(
		request,
		'index.html',
		)


class SkatersListView(generic.ListView):
	model = skater
	

class SkatersDetailView(generic.DetailView):
	model = skater


class TrainersListView(generic.ListView):
	model = trainer


class TrainersDetailView(generic.DetailView):
	model = trainer


class ElementsListView(generic.ListView):
	model = element


class ElementsDetailView(generic.DetailView):
	model = element


