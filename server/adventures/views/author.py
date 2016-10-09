"""
Views for the Author endpoint.
"""
from rest_framework import viewsets
from ..models import Author
from ..serializers.author import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    Views for the Author endpoint.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
