"""
Serializer for the Environment model.
"""
from rest_framework import serializers
from ..models import Environment


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Environment model.
    """
    class Meta:
        model = Environment
        depth = 1
