from rest_framework import serializers
from .models import Author, Publisher, Adventure


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class AdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventure
        depth = 2
