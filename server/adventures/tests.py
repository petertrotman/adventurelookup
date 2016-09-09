from django.test import TestCase
from .models import Author, Publisher, Edition, Setting, Adventure


class AuthorTests(TestCase):
    def setUp(self):
        self.gygax = Author.objects.create(name='Gary Gygax')

    def test_create_author(self):
        self.assertEqual(Author.objects.first(), self.gygax)
        self.assertEqual(Author.objects.count(), 1)

    def test_update_author(self):
        Author.objects.filter(id=self.gygax.id).update(name='Joe Bloggs')
        self.assertEqual(Author.objects.first().name, 'Joe Bloggs')

    def test_delete_author(self):
        Author.objects.filter(id=self.gygax.id).delete()
        self.assertEqual(Author.objects.count(), 0)
