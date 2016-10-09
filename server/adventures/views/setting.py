"""
Views for the Setting endpoint.
"""
from rest_framework import viewsets
from ..models import Setting
from ..serializers.setting import SettingSerializer


class SettingViewSet(viewsets.ModelViewSet):
    """
    Views for the Setting endpoint.
    """
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
