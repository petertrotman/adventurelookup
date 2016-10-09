"""
Serializer for the ItemModifier model.
"""
from rest_framework import serializers
from ..models import ItemModifier


class ItemModifierSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the ItemModifier model.
    """
    class Meta:
        model = ItemModifier
        depth = 1
