from collections import OrderedDict
from datetime import date
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from adventures.models import Adventure, Setting, Edition, Author, Publisher
from adventures.views import AdventureList


class AdventureListTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        realms = Setting.objects.create(name='Forgotten Realms')
        fifth_edition = Edition.objects.create(name='5th Edition')
        perkins = Author.objects.create(name='Chris Perkins')
        wotc = Publisher.objects.create(name='Wizards of the Coast')
        self.oota = Adventure.objects.create(title='Out of the Abyss',
                                             setting=realms,
                                             publisher=wotc,
                                             edition=fifth_edition,
                                             published=date(2014, 7, 22),
                                             min_level=1,
                                             max_level=15,
                                             min_characters=2,
                                             max_characters=5)
        self.oota.authors.add(perkins)

    def test_get(self):
        request = self.factory.get('/adventures/adventures')
        response = AdventureList.as_view()(request)
        # Ignoring created and last_modified because they will change every
        # time the test is run.
        data_should_be = OrderedDict([
            ('count', 1), ('next', None), ('previous', None),
            ('results', [OrderedDict([
                ('id', 5),
                ('authors',
                 [OrderedDict([('id', 6), ('name', 'Chris Perkins')])]),
                ('publisher',
                 OrderedDict([('id', 6), ('name', 'Wizards of the Coast')])),
                ('edition', OrderedDict([('id', 6), ('name', '5th Edition')])),
                ('setting',
                 OrderedDict([('id', 6), ('name', 'Forgotten Realms')])),
                ('title', 'Out of the Abyss'), ('published', '2014-07-22'),
                ('min_level', 1), ('max_level', 15), ('min_characters', 2),
                ('max_characters', 5)
            ])])
        ])
        actual_data = response.data
        del actual_data['results'][0]['created']
        del actual_data['results'][0]['last_modified']
        self.assertEqual(actual_data, data_should_be)

    def test_post(self):
        test_data = {'title': 'lmop',
                     'authors': [{'name': 'gygax'}],
                     'publisher': {'name': 'wotc'},
                     'edition': {'name': '5e'},
                     'setting': {'name': 'forgotten realms'},
                     'published': date(2015, 1, 1),
                     'min_level': 1,
                     'max_level': 5,
                     'min_characters': 1,
                     'max_characters': 5}
        request = self.factory.post('/adventures/adventures',
                                    test_data,
                                    format='json')
        response = AdventureList.as_view()(request)
        # Ignoring created and last_modified because they will change every
        # time the test is run.
        actual_data = response.data
        del actual_data['created']
        del actual_data['last_modified']
        self.assertEqual(response.data, {
            'id': 7,
            'min_characters': 1,
            'max_characters': 5,
            'title': 'lmop',
            'min_level': 1,
            'published': '2015-01-01',
            'max_level': 5,
            'edition': OrderedDict([('id', 8), ('name', '5e')]),
            'publisher': OrderedDict([('id', 8), ('name', 'wotc')]),
            'authors': [OrderedDict([('id', 8), ('name', 'gygax')])],
            'setting': OrderedDict([('id', 8), ('name', 'forgotten realms')])
        })
