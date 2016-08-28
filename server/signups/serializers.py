"""Serializers for the models."""
# pylint: disable=missing-docstring,too-few-public-methods
from rest_framework import serializers
from . import models

class SignupSerializer(serializers.ModelSerializer):
    """Serializer for the Signup model."""
    class Meta:
        model = models.Signup
        fields = ('id', 'created_at', 'email')
