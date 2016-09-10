from rest_framework import serializers
from .models import Author, Publisher, Edition, Setting, Adventure


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting


class AdventureSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()
    edition = EditionSerializer()
    setting = SettingSerializer()

    class Meta:
        model = Adventure

    def create(self, validated_data):
        # Remove and store data for related objects from validated_data.
        authors_data = validated_data.pop('authors')
        publisher_data = validated_data.pop('publisher')
        edition_data = validated_data.pop('edition')
        setting_data = validated_data.pop('setting')

        # Get or create related objects.
        authors = []
        for author_data in authors_data:
            author, _ = Author.objects.get_or_create(**author_data)
            authors.append(author)
        publisher, _ = Publisher.objects.get_or_create(**publisher_data)
        edition, _ = Edition.objects.get_or_create(**edition_data)
        setting, _ = Setting.objects.get_or_create(**setting_data)

        # Add related objects themselves back into validated_data and create
        # an Adventure object.
        validated_data['publisher'] = publisher
        validated_data['edition'] = edition
        validated_data['setting'] = setting
        adventure = Adventure.objects.create(**validated_data)
        # Authors are a ManyToMany relation, so they must be added after
        # creation.
        adventure.authors.set(authors)
        return adventure

    def update(self, instance, validated_data):
        # Get the updated_data out of validated_data, if it's there.
        updated_data = {}
        for field in ('authors', 'publisher', 'edition', 'setting'):
            try:
                updated_data[field] = validated_data.pop('field')
            except KeyError:
                updated_data[field] = None

        # Get updated values for fields if they exist, otherwise use those from
        # instance.
        if updated_data['authors'] is not None:
            authors = []
            for author_data in updated_data['authors']:
                author, _ = Author.objects.get_or_create(**author_data)
                authors.append(author)
        else:
            authors = instance.authors.all()

        if updated_data['publisher'] is not None:
            publisher, _ = Publisher.objects.get_or_create(**updated_data['publisher'])     # noqa
        else:
            publisher = instance.publisher

        if updated_data['edition'] is not None:
            edition, _ = Edition.objects.get_or_create(**updated_data['edition'])   # noqa
        else:
            edition = instance.edition

        if updated_data['setting'] is not None:
            setting, _ = Setting.objects.get_or_create(**updated_data['setting'])   # noqa
        else:
            setting = instance.setting

        instance.title = validated_data.get('title', instance.title)
        instance.title = validated_data.get('published', instance.published)
        instance.title = validated_data.get('min_level', instance.min_level)
        instance.title = validated_data.get('max_level', instance.max_level)
        instance.title = validated_data.get('min_characters',
                                            instance.min_characters)
        instance.title = validated_data.get('max_characters',
                                            instance.max_characters)
        instance.publisher = publisher
        instance.edition = edition
        instance.setting = setting
        instance.authors.set(authors)
        instance.save()
        return instance
