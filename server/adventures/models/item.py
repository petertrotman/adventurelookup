"""
Model for the items.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin, DescriptionNotesMixin


class Item(models.Model, TimestampMixin, DescriptionNotesMixin):
    """
    Model for the items.
    """

    name = models.CharField(max_length=128)
    type = models.ForeignKey('ItemType', models.PROTECT,
                             related_name='items')
    modifier = models.ForeignKey('ItemModifier', models.PROTECT,
                                 related_name='items',
                                 blank=True, null=True)

    adventure_item = models.BooleanField(default=False,
                                         help_text='Flag to state whether the'
                                         'item is an adventure item - i.e.'
                                         'specific to the adventure in which'
                                         'it appears')
