"""
Views for the Race endpoint.
"""
from rest_framework import viewsets
from ..models import Race
from ..serializers.race import RaceSerializer


class RaceViewSet(viewsets.ModelViewSet):
    """
    Views for the Race endpoint.
    """
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
