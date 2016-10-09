"""
Views for the Item endpoint.
"""
from rest_framework import viewsets
from ..models import Item
from ..serializers.item import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    Views for the Item endpoint.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
