"""
Model for the adventure.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Adventure(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the adventure.
    """

    name = models.CharField(max_length=128)
    setting = models.ForeignKey('Setting', models.PROTECT,
                                related_name='adventures')

    edition = models.ForeignKey('Edition', models.PROTECT,
                                related_name='adventures')
    author = models.ForeignKey('Author', models.PROTECT,
                               related_name='adventures')
    publisher = models.ForeignKey('Publisher', models.PROTECT,
                                  related_name='adventures')
    date = models.DateField()

    characters = models.ManyToManyField('Character', related_name='adventures')
    monsters = models.ManyToManyField('Monster', related_name='adventures')
    items = models.ManyToManyField('Item', related_name='adventures')

    format = models.CharField(max_length=128)
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    min_characters = models.IntegerField()
    max_characters = models.IntegerField()
