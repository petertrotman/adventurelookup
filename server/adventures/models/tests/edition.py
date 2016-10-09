# pylint: disable=missing-docstring
from django.test import TestCase
from ..edition import Edition


class EditionTestCase(TestCase):
    def test_create_edition(self):
        odandd = Edition.objects.create(name='OD&D')
        self.assertEqual(Edition.objects.first(), odandd)
        self.assertEqual(Edition.objects.count(), 1)
