"""
Model for the setting.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Setting(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the setting.
    """

    name = models.CharField(max_length=128)
    environment = models.ForeignKey('Environment', models.PROTECT,
                                    related_name='settings')
