"""
Views for the Adventure endpoint.
"""
from rest_framework import viewsets
from ..models import Adventure
from ..serializers.adventure import AdventureSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    """
    Views for the Adventure endpoint.
    """
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer
