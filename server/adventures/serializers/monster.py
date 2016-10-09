"""
Serializer for the Monster model.
"""
from rest_framework import serializers
from ..models import Monster


class MonsterSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Monster model.
    """
    class Meta:
        model = Monster
        depth = 1
