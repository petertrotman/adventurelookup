"""
Model for the character races.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Race(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the character races.
    """

    name = models.CharField(max_length=128)
