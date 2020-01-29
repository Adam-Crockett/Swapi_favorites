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
        films_list = self.cache_handler.get_cache('films')
        new_hope_test = self.detail_gathering.item_handler(
            films_list, 'films', 'A New Hope')

        new_hope_data = self.detail_gathering.film_handler(new_hope_test)

        self.assertIsNot(new_hope_data, False)

    def test_people_handler_success(self):
        people_list = self.cache_handler.get_cache('people')
        yoda_test = self.detail_gathering.item_handler(
            people_list, 'people', 'Yoda')

        yoda_data = self.detail_gathering.people_handler(yoda_test)

        self.assertIsNot(yoda_data, False)

    def test_species_handler_success(self):
        species_list = self.cache_handler.get_cache('species')
        human_test = self.detail_gathering.item_handler(
            species_list, 'species', 'Human')

        human_data = self.detail_gathering.species_handler(human_test)

        self.assertIsNot(human_data, False)

    def test_starship_handler_success(self):
        starship_list = self.cache_handler.get_cache('starships')
        x_wing_test = self.detail_gathering.item_handler(
            starship_list, 'starships', 'X-wing')

        x_wing_data = self.detail_gathering.starship_handler(x_wing_test)

        self.assertIsNot(x_wing_data, False)

    def test_planet_handler_success(self):
        planets_list = self.cache_handler.get_cache('planets')
        coruscant_test = self.detail_gathering.item_handler(
            planets_list, 'planets', 'Coruscant')

        coruscant_data = self.detail_gathering.planet_handler(coruscant_test)

        self.assertIsNot(coruscant_data, False)

    def test_vehicle_handler_success(self):
        vehicle_list = self.cache_handler.get_cache('vehicles')
        snowspeeder_test = self.detail_gathering.item_handler(
            vehicle_list, 'vehicles', 'Snowspeeder')

        snowspeeder_data = self.detail_gathering.vehicle_handler(
            snowspeeder_test)

        self.assertIsNot(snowspeeder_data, False)
