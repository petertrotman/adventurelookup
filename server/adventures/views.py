from adventures.models import Adventure
from adventures.serializers import AdventureSerializer
from rest_framework import generics


class AdventureList(generics.ListCreateAPIView):
    '''API view for listing existing adventures and creating new ones.'''
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer
