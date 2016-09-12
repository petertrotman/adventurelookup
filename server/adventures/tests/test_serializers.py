from datetime import date
from django.test import TestCase
from adventures.models import Adventure, Edition, Publisher, Author, Setting
from adventures.serializers import AdventureSerializer


class AdventureSerializerTestCase(TestCase):

    def setUp(self):
        self.test_data = {'title': 'lmop',
                          'authors': [{'name': 'gygax'}],
                          'publisher': {'name': 'wotc'},
                          'edition': {'name': '5e'},
                          'setting': {'name': 'forgotten realms'},
                          'published': date(2015, 1, 1),
                          'min_level': 1, 'max_level': 5,
                          'min_characters': 1,
                          'max_characters': 5
                          }
        realms = Setting.objects.create(name='Forgotten Realms')
        fifth_edition = Edition.objects.create(name='5th Edition')
        perkins = Author.objects.create(name='Chris Perkins')
        wotc = Publisher.objects.create(name='Wizards of the Coast')
        self.existing_adventure = Adventure.objects.create(
            title='Out of the Abyss',
            setting=realms,
            publisher=wotc,
            edition=fifth_edition,
            published=date(2014, 7, 22),
            min_level=1,
            max_level=15,
            min_characters=2,
            max_characters=5)
        self.existing_adventure.authors.add(perkins)

    def test_create(self):
        lmop = AdventureSerializer(data=self.test_data)
        lmop.is_valid()
        lmop.save()
        should_be_test_adv = Adventure.objects.last()
        self.assertEqual(should_be_test_adv.title, self.test_data['title'])
        self.assertEqual(should_be_test_adv.published,
                         self.test_data['published'])
        self.assertEqual(should_be_test_adv.min_level,
                         self.test_data['min_level'])
        self.assertEqual(should_be_test_adv.max_level,
                         self.test_data['max_level'])
        self.assertEqual(should_be_test_adv.min_characters,
                         self.test_data['min_characters'])
        self.assertEqual(should_be_test_adv.max_characters,
                         self.test_data['max_characters'])
        self.assertEqual(list(should_be_test_adv.authors.all()),
                         [Author.objects.get(name='gygax')])
        self.assertEqual(should_be_test_adv.publisher,
                         Publisher.objects.get(name='wotc'))
        self.assertEqual(should_be_test_adv.edition,
                         Edition.objects.get(name='5e'))
        self.assertEqual(should_be_test_adv.setting,
                         Setting.objects.get(name='forgotten realms'))

    def test_update(self):
        oota = Adventure.objects.get(title='Out of the Abyss')
        oota.title = 'Tyranny of Dragons'
        oota.save()
        updated_oota = Adventure.objects.get(published=date(2014, 7, 22))
        self.assertEqual(updated_oota.title, 'Tyranny of Dragons')
