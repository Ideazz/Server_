from django.conf.urls import url
from .views import EntrepreneurCreateView,EntrepreneurPutView


urlpatterns = [

    url(r'^api/entrepreneur/(?P<pk>[0-9]+)/$', EntrepreneurPutView.as_view(), name='entrepreneur-profile-put'),
    url(r'^api/entrepreneur/(?P<pk>[0-9]+)/$', EntrepreneurCreateView.as_view(), name='entrepreneur-profile-create'),

]
