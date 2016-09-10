from rest_framework import serializers
from .models import Author, Adventure


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class AdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventure
        depth = 2
