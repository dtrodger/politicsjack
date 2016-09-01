from django.conf.urls import url

from .views import EventDetail, EventList

urlpatterns = [

	# url(r'create/$', CauseCreate.as_view(), name="cause_create"),

	url(r'list/$', EventList.as_view(), name="event_list"),

	# url(r'user_list/$', UserCauseList.as_view(), name="user_cause_list"),

	# url(r'^update/(?P<slug>[\w-]+)/$', CauseUpdate.as_view(), name="cause_update"),

	# url(r'^delete/(?P<slug>[\w-]+)/$', CauseDelete.as_view(), name="cause_delete"),

	url(r'^(?P<slug>[\w-]+)/$', EventDetail.as_view(), name="event_detail"),

]