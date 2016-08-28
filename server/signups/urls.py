"""
URL definitions for the Signups API.
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^', views.SignupView.as_view()),
]
