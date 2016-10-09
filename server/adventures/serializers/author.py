"""
Serializer for the Author model.
"""
from rest_framework import serializers
from ..models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Author model.
    """
    class Meta:
        model = Author
        depth = 1
