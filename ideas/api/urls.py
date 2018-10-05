from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/ideas/$', views.apilist),
    url(r'^api/ideas/(?P<pk>[0-9]+)/$', views.apidetails),
    url(r'^api/ideas/user/(?P<pk>[0-9]+)/$', views.apibyuserdetails),
]
