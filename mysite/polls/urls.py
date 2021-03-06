#from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views
app_name = 'polls'
urlpatterns = [
	#path('', views.index, name = 'index'),
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	
	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
]
