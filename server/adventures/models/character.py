"""
Model for the characters.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Character(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the characters.
    """
    name = models.CharField(max_length=128)
    level = models.IntegerField()
    race = models.ForeignKey('Race', models.PROTECT,
                             related_name='characters')
