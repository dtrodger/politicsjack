from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import Notification
from .forms import NotificationCreationForm


class NotificationCreate(LoginRequiredMixin, CreateView):
	model = Notification
	form_class = NotificationCreationForm
	template_name = "notification/notification_form.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('notification_detail', args=[self.object.slug])


class NotificationUpdate(UpdateView):
	model = Notification
	template_name = "notification/notification_update.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('notification_detail', args=[self.object.slug])


class NotificationDetail(DetailView):
	model = Notification
	template_name = "notification/notification_detail.html"


class NotificationList(ListView):
	model = Notification
	template_name = "notification/notification_list.html"


class UserNotificationList(LoginRequiredMixin, ListView):
	model = Notification
	template_name = "notification/user_notification_list.html"


class NotificationDelete(DeleteView):
	model = Notification
	template_name = "notification/notification_delete.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('notification_list')