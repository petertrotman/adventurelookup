"""
Views for the Monster endpoint.
"""
from rest_framework import viewsets
from ..models import Monster
from ..serializers.monster import MonsterSerializer


class MonsterViewSet(viewsets.ModelViewSet):
    """
    Views for the Monster endpoint.
    """
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
