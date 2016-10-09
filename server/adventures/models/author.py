"""
Model for the author.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Author(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the author.
    """

    name = models.CharField(max_length=128)
