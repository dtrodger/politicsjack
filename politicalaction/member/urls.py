from django.conf.urls import url

from .views import MemberCreateView, MemberDetailView, MemberNeededView, MemberUpdate

urlpatterns = [

	url(r'^create/$', MemberCreateView.as_view(), name="member_create"),

	url(r'^restricted/$', MemberNeededView.as_view(), name="member_needed"),

	url(r'^update/(?P<slug>[\w-]+)/$', MemberUpdate.as_view(), name="member_update"),

	# url(r'^delete/(?P<slug>[\w-]+)/$', MemberDelete.as_view(), name="member_delete"),

	url(r'^(?P<slug>[\w-]+)/(?P<id>[\d-]+)/$', MemberDetailView.as_view(), name="member_detail"),

]