# pylint: disable=missing-docstring
from django.test import TestCase
from ..publisher import Publisher


class PublisherTestCase(TestCase):
    def test_create_publisher(self):
        wotc = Publisher.objects.create(name='Wizards of the Coast')
        self.assertEqual(Publisher.objects.first(), wotc)
        self.assertEqual(Publisher.objects.count(), 1)
