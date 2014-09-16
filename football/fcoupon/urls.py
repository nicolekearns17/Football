from django.conf.urls import patterns, url
from fcoupon import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))
