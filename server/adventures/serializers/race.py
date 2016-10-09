"""
Serializer for the Race model.
"""
from rest_framework import serializers
from ..models import Race


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Race model.
    """
    class Meta:
        model = Race
        depth = 1
