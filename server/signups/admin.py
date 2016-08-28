"""
Admin model registration for the Signups API.
"""
from django.contrib import admin
from . import models

admin.site.register(models.Signup)
