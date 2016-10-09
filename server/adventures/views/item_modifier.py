"""
Views for the ItemModifier endpoint.
"""
from rest_framework import viewsets
from ..models import ItemModifier
from ..serializers.item_modifier import ItemModifierSerializer


class ItemModifierViewSet(viewsets.ModelViewSet):
    """
    Views for the ItemModifier endpoint.
    """
    queryset = ItemModifier.objects.all()
    serializer_class = ItemModifierSerializer
