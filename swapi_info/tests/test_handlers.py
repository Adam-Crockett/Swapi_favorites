from django.test import TestCase, Client
from django.urls import reverse
import json
from swapi_info import handlers


class TestHandlers(TestCase):
    """
    Handler Test Cases.
    """

    def setUp(self):
        """
        Create starting paramaters for handler tests.
        """

    def test_set_cache_successful(self):
        pass

    def test_set_cahce_failure(self):
        pass

    def test_get_cache_type_does_not_exist(self):
        pass

    def test_get_cahce_type_type_does_exist(self):
        pass

    def test_handle_bad_name_change(self):
        pass

    def test_item_handler_successful(self):
        pass

    def test_item_handler_failure(self):
        pass

    def test_film_handler_success(self):
        pass

    def test_people_handler_success(self):
        pass

    def test_species_handler_success(self):
        pass

    def test_starship_handler_success(self):
        pass

    def test_planet_handler_success(self):
        pass

    def test_vehicle_handler_success(self):
        pass
