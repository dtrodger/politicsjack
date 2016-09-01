from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import Cause
from .forms import CauseCreationForm

from notification.models import Notification


# class CauseCreate(LoginRequiredMixin, CreateView):
# 	model = Cause
# 	form_class = CauseCreationForm
# 	template_name = "cause/cause_form.html"

# 	def get_success_url(self, **kwargs):
# 		return reverse_lazy('cause_detail', args=[self.object.slug])


class CauseUpdate(UpdateView):
	model = Cause
	template_name = "cause/cause_update.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('cause_detail', args=[self.object.slug])


class CauseDetail(DetailView):
	model = Cause
	template_name = "cause/cause_detail.html"

	def get_context_data(self, **kwargs):
		context = super(CauseDetail, self).get_context_data(**kwargs)
		print self.object
		notifications = Notification.objects.filter(cause = self.object)
		context['notifications'] = notifications

		return context


class CauseList(ListView):
	model = Cause
	template_name = "cause/cause_list.html"


class UserCauseList(LoginRequiredMixin, ListView):
	model = Cause
	template_name = "cause/user_cause_list.html"


class CauseDelete(DeleteView):
	model = Cause
	template_name = "cause/cause_delete.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('cause_list')


