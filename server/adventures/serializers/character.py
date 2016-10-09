"""
Serializer for the Character model.
"""
from rest_framework import serializers
from ..models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Character model.
    """
    class Meta:
        model = Character
        depth = 1
