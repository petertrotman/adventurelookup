# pylint: disable=missing-docstring
from django.test import TestCase
from ..author import Author


class AuthorTestCase(TestCase):
    def test_create_author(self):
        gygax = Author.objects.create(name='Gary Gygax')
        self.assertEqual(Author.objects.first(), gygax)
        self.assertEqual(Author.objects.count(), 1)
