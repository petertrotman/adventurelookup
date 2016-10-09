"""
Serializer for the Edition model.
"""
from rest_framework import serializers
from ..models import Edition


class EditionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Edition model.
    """
    class Meta:
        model = Edition
        depth = 1
