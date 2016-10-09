"""
Views for the Publisher endpoint.
"""
from rest_framework import viewsets
from ..models import Publisher
from ..serializers.publisher import PublisherSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    Views for the Publisher endpoint.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
