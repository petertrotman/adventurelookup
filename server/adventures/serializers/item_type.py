"""
Serializer for the ItemType model.
"""
from rest_framework import serializers
from ..models import ItemType


class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the ItemType model.
    """
    class Meta:
        model = ItemType
        depth = 1
