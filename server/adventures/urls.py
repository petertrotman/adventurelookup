from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from adventures import views

urlpatterns = format_suffix_patterns([
    url(r'^adventures/$', views.AdventureList.as_view(),
        name='adventure-list'),
])
