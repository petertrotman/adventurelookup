"""
Model for the publisher.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Publisher(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the publisher.
    """

    name = models.CharField(max_length=128)
