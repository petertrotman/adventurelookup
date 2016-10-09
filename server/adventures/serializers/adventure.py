"""
Serializer for the Adventure model.
"""
from rest_framework import serializers
from ..models import Adventure


class AdventureSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Adventure model.
    """
    class Meta:
        model = Adventure
        depth = 1
