"""
Serializer for the Setting model.
"""
from rest_framework import serializers
from ..models import Setting


class SettingSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Setting model.
    """
    class Meta:
        model = Setting
        depth = 1
