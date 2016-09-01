from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy

from politicalaction.mixins import MemberRequiredMixin

from .models import Member
from .forms import MemberModelForm


class MemberCreateView(LoginRequiredMixin, CreateView):
	model = Member
	form_class = MemberModelForm
	template_name = "member/member_form.html"

	def form_valid(self, form):
		member = form.save(commit=False)
		member.user = self.request.user
		return super(MemberCreateView, self).form_valid(form)

	def get_success_url(self, **kwargs):
		return reverse_lazy('member_detail', args=[self.object.slug])


class MemberNeededView(TemplateView):
	template_name = "member/member_needed.html"


class MemberUpdate(UpdateView):
	model = Member
	template_name = "member/meMemberupdate.html"

	def get_success_url(self, **kwargs):
		return reverse_lazy('member_detail', args=[self.object.slug])


class MemberDetailView(DetailView, MemberRequiredMixin):
	model = Member
	template_name = "member/member_detail.html"

	def get_context_data(self, **kwargs):
		context = super(MemberDetailView, self).get_context_data(**kwargs)
		print self.object.causes.all
		if self.object.causes.all:
			causes = self.object.causes.all
			context["causes"] = causes
		return context


# class MemberDelete(DeleteView):
# 	model = Cause
# 	template_name = "member/member_delete.html"

# 	def get_success_url(self, **kwargs):
# 		return reverse_lazy('cause_list')


