from django.conf.urls import url

from .views import NotificationCreate, NotificationUpdate, NotificationDetail, NotificationList, UserNotificationList, NotificationDelete

urlpatterns = [

	url(r'create/$', NotificationCreate.as_view(), name="notification_create"),

	url(r'list/$', NotificationList.as_view(), name="notification_list"),

	url(r'user_list/$',NotificationList.as_view(), name="user_notification_list"),

	url(r'^update/(?P<slug>[\w-]+)/$', NotificationUpdate.as_view(), name="notification_update"),

	url(r'^delete/(?P<slug>[\w-]+)/$', NotificationDelete.as_view(), name="notification_delete"),

	url(r'^(?P<slug>[\w-]+)/$', NotificationDetail.as_view(), name="notification_detail"),

]