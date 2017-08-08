from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from search.models import Contractor

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Contractor.objects.all().order_by("ratings")[:25], template_name="search/search.html"), name='homepage'),

	# The primary key is a digit and is increasing, otherwise don't return anything
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Contractor, template_name='search/contractor_details.html'))
]