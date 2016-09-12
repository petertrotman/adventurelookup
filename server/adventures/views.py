'''
API views.

AdventureList: API view for listing existing adventures and creating new ones.
'''
from adventures.models import Adventure
from adventures.serializers import AdventureSerializer
from rest_framework import generics


class AdventureList(generics.ListCreateAPIView):
    '''API view for listing existing adventures and creating new ones.'''
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer


class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    '''API view for retrieving, updating or deleting a single adventure.'''
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer
