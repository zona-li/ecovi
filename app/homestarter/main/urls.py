from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='homepage'),
	url(r'^about/$', views.about, name='about'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^linkedin/$', views.linkedin, name='linkedin'),
	url(r'^facebook/$', views.facebook, name='facebook'),
	url(r'^instagram/$', views.instagram, name='instagram'),
]