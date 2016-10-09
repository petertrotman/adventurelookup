"""
Model for the item types.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class ItemType(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the item types.
    """

    name = models.CharField(max_length=128)
