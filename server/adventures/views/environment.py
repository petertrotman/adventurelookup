"""
Views for the Environment endpoint.
"""
from rest_framework import viewsets
from ..models import Environment
from ..serializers.environment import EnvironmentSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    """
    Views for the Environment endpoint.
    """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
