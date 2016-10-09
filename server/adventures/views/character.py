"""
Views for the Character endpoint.
"""
from rest_framework import viewsets
from ..models import Character
from ..serializers.character import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    """
    Views for the Character endpoint.
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
