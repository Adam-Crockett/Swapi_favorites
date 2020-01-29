from django.test import TestCase, Client
from django.urls import reverse
import json
from swapi_info.handlers import CacheController, DetailGathering


class TestHandlers(TestCase):
    """
    Handler Test Cases.
    """

    def setUp(self):
        """
        Create starting paramaters for handler tests.
        """
        self.cache_handler = CacheController()
        self.detail_gathering = DetailGathering()
        self.planet_list = self.cache_handler.get_cache('planets')

    def test_get_cache_type_does_not_exist(self):
        invalid_search = self.cache_handler.get_cache('Not valid search type')

        self.assertFalse(invalid_search, False)

    def test_get_cahce_type_type_does_exist(self):
        valid_search = self.cache_handler.get_cache('films')

        self.assertIsNot(valid_search, False)

    def test_item_handler_successful(self):
        valid_item = self.detail_gathering.item_handler(
            self.planet_list, 'planets', 'Naboo')

        self.assertIsNot(valid_item, False)

    def test_item_handler_bad_name_faliure(self):
        valid_item = self.detail_gathering.item_handler(
            self.planet_list, 'planets', 'Not a planet Name')

        self.assertEquals(valid_item, False)

    def test_item_handler_bad_type_faliure(self):
        valid_item = self.detail_gathering.item_handler(
            self.planet_list, 'bad search type', 'Naboo')

        self.assertEquals(valid_item, False)

    def test_film_handler_success(self):
        pass

    def test_people_handler_success(self):
        pass

    def test_species_handler_success(self):
        pass

    def test_starship_handler_success(self):
        pass

    def test_planet_handler_success(self):
        planets_list = self.cache_handler.get_cache('planets')
        coruscant_test = self.detail_gathering.item_handler(
            planets_list, 'planets', 'coruscant')

        self.assertIsNot(coruscant_test, False)

    def test_vehicle_handler_success(self):
        pass
