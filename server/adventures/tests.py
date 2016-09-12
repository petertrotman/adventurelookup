"""
Tests for the Adventures app.
"""
# pylint: disable=missing-docstring
from datetime import date
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


class EditionTests(TestCase):
    def test_create_author(self):
        odandd = Edition.objects.create(name='OD&D')
        self.assertEqual(Edition.objects.first(), odandd)
        self.assertEqual(Edition.objects.count(), 1)


class SettingTests(TestCase):
    def test_create_author(self):
        forgotten_realms = Setting.objects.create(name='Forgotten Realms')
        self.assertEqual(Setting.objects.first(), forgotten_realms)
        self.assertEqual(Setting.objects.count(), 1)


class AdventureTests(TestCase):
    def test_create_author(self):
        fifth_ed = Edition.objects.create(name='D&D 5th Edition')
        wotc = Publisher.objects.create(name='Wizards of the Coast')
        forgotten_realms = Setting.objects.create(name='Forgotten Realms')

        lmop = Adventure.objects.create(
            title='Lost Mines of Phandelver',
            edition=fifth_ed,
            publisher=wotc,
            setting=forgotten_realms,
            published=date(2014, 1, 1),
            min_level=1,
            max_level=5,
            min_characters=3,
            max_characters=5)
        lmop.authors.create(name='Gary Gygax')
        self.assertEqual(Adventure.objects.first(), lmop)
        self.assertEqual(Adventure.objects.count(), 1)
