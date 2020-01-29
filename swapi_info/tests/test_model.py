from django.test import TestCase
from swapi_info.models import Favorites


class TestModels(TestCase):
    """
    Model Test Cases.
    """

    def setUp(self):
        self.existing_yoda_favorite = Favorites.objects.create(
            name='Yoda',
            item_type='people',
            swapi_url='https://swapi.co/api/people/20/',
            favorite_count=1
        )

    def test_create_new_favorite(self):
        new_favorite = Favorites.objects.create(
            name='A New Hope',
            item_type='films',
            swapi_url='https://swapi.co/api/films/1/',
            favorite_count=1
        )

        self.assertEquals(new_favorite.name, 'A New Hope')
        self.assertEquals(new_favorite.item_type, 'films')
        self.assertEquals(new_favorite.swapi_url,
                          'https://swapi.co/api/films/1/')
        self.assertEquals(new_favorite.favorite_count, 1)

    def test_increment_current_favorite(self):
        self.existing_yoda_favorite.favorite_count += 1

        self.assertEquals(self.existing_yoda_favorite.favorite_count, 2)
