"""
Model for the item modifiers.
"""
# pylint: disable=too-few-public-methods
from django.db import models
from .mixins import TimestampMixin


class ItemModifier(models.Model, TimestampMixin):
    """
    Model for the item modifiers.
    """
    ATTACK = 'ATK'
    DAMAGE = 'DMG'
    STRENGTH = 'STR'
    DEXTERITY = 'DEX'
    CONSTITUTION = 'CON'
    INTELLIGENCE = 'INT'
    WISDOM = 'WIS'
    CHARISMA = 'CHA'

    STAT_CHOICES = (
        (ATTACK, 'Attack'),
        (DAMAGE, 'Damage'),
        (STRENGTH, 'Strength'),
        (DEXTERITY, 'Dexterity'),
        (CONSTITUTION, 'Constitution'),
        (INTELLIGENCE, 'Intelligence'),
        (WISDOM, 'Wisdom'),
        (CHARISMA, 'Charisma'),
    )

    stat = models.CharField(max_length=3, choices=STAT_CHOICES)
    value = models.IntegerField()
    condition = models.CharField(max_length=128)
