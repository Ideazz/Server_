from django.conf.urls import url
from .views import IdeatorPutViews,IdeatorCreateViews

urlpatterns = [

    url(r'^api/ideator/(?P<pk>[0-9]+)/$', IdeatorPutViews.as_view(), name='entrepreneur-profile-put'),
    url(r'^api/ideator/(?P<pk>[0-9]+)/$', IdeatorCreateViews.as_view(), name='entrepreneur-profile-create'),

]
