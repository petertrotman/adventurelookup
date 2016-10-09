"""
Mixins for other models to build upon.
"""
# pylint: disable=too-few-public-methods
from django.db import models


class TimestampMixin:
    """
    Includes basic timestamp information for the model.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DescriptionNotesMixin:
    """
    Includes both a description and a notes field.
    The Description is for providing a description for the item.
    The Notes is for any notes related to the item.
    """

    description = models.TextField(default='')
    notes = models.TextField(default='')
