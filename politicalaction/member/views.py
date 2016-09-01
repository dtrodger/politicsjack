from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import Member
from .forms import MemberCreationForm


class MemberCreate(LoginRequiredMixin, CreateView):
	model = Member
	form_class = MemberCreationForm
	template_name = "member/member_form.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('member_detail', args=[self.object.slug])


class MemberUpdate(UpdateView):
	model = Member
	template_name = "member/meMemberupdate.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('member_detail', args=[self.object.slug])


class MemberDetail(DetailView):
	model = Member
	template_name = "member/member_detail.html"


class MemberDelete(DeleteView):
	model = Cause
	template_name = "member/member_delete.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('cause_list')


