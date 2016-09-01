from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView

from .models import Event


class EventDetail(DetailView):
	model = Event
	template_name = "event/event_detail.html"


class EventList(ListView):
	model = Event
	template_name = "event/event_list.html"