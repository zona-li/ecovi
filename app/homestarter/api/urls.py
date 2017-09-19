from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^project/$', CreateView.as_view(), name="create"),
    url(r'^project/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),	# This includes the DRF routes that provides a default login template to authenticate a user.
    # url(r'^users/$', UserView.as_view(), name="users"),
    # url(r'users/(?P<pk>[0-9]+/$', UserDetailsView.as_view, name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)