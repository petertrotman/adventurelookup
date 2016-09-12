"""
URL definitions for the Signups API.
"""
from django.conf.urls import url
from . import views

urlpatterns = [  # pylint: disable=invalid-name
    url('^', views.SignupView.as_view()),
]
