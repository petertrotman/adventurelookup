"""
Views for the ItemType endpoint.
"""
from rest_framework import viewsets
from ..models import ItemType
from ..serializers.item_type import ItemTypeSerializer


class ItemTypeViewSet(viewsets.ModelViewSet):
    """
    Views for the ItemType endpoint.
    """
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer
