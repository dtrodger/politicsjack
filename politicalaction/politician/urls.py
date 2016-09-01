from django.conf.urls import url

from .views import PoliticianDetail, PoliticianList

urlpatterns = [

	url(r'list/$', PoliticianList.as_view(), name="politician_list"),

	url(r'^(?P<slug>[\w-]+)/$', PoliticianDetail.as_view(), name="politician_detail"),

]