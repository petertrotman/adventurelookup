"""
Serializer for the Item model.
"""
from rest_framework import serializers
from ..models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Item model.
    """
    class Meta:
        model = Item
        depth = 1
