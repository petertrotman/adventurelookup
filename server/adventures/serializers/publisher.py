"""
Serializer for the Publisher model.
"""
from rest_framework import serializers
from ..models import Publisher


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Publisher model.
    """
    class Meta:
        model = Publisher
        depth = 1
