from django.shortcuts import redirect

class MemberRequiredMixin(object):
	def dispatch(self, request, *args, **kwargs):
		if not request.user.member:
			return redirect("member_needed")
		return super(MemberRequiredMixin, self).dispatch(request, *args, **kwargs)
