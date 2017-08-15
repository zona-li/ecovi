from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signup_confirm/', views.signup_confirm, name='signup_confirm'),
]