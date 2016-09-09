from django.test import TestCase
from .models import Author, Publisher, Edition, Setting, Adventure


class AuthorTests(TestCase):
    def test_create_author(self):
        gygax = Author.objects.create(name='Gary Gygax')
        self.assertEqual(Author.objects.first(), gygax)
        self.assertEqual(Author.objects.count(), 1)


class PublisherTests(TestCase):
    def test_create_author(self):
        wotc = Publisher.objects.create(name='Wizards of the Coast')
        self.assertEqual(Publisher.objects.first(), wotc)
        self.assertEqual(Publisher.objects.count(), 1)
