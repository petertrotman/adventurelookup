"""
Model for the edition.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Edition(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the edition.
    """

    name = models.CharField(max_length=128)
