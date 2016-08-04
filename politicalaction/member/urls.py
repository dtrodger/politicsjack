from django.conf.urls import url

from .views import MemberCreate, MemberUpdate, MemberDetail, MemberDelete

urlpatterns = [

	url(r'create/$', MemberCreate.as_view(), name="member_create"),

	url(r'^update/(?P<slug>[\w-]+)/$', MemberUpdate.as_view(), name="member_update"),

	url(r'^delete/(?P<slug>[\w-]+)/$', MemberDelete.as_view(), name="member_delete"),

	url(r'^(?P<slug>[\w-]+)/$', MemberDetail.as_view(), name="member_detail"),

]