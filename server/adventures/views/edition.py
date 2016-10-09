"""
Views for the Edition endpoint.
"""
from rest_framework import viewsets
from ..models import Edition
from ..serializers.edition import EditionSerializer


class EditionViewSet(viewsets.ModelViewSet):
    """
    Views for the Edition endpoint.
    """
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
