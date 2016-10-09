"""
Model for the environments.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Environment(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the environments.
    """

    name = models.CharField(max_length=128)
