from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView

from .models import Politician


class PoliticianDetail(DetailView):
	model = Politician
	template_name = "politician/politician_detail.html"


class PoliticianList(ListView):
	model = Politician
	template_name = "politician/politician_list.html"