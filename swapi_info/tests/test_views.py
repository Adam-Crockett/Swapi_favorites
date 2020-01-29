from django.test import TestCase, Client
from django.urls import reverse
from swapi_info.views import HomePage, search, ResultList, ItemDetails, add_favorite
import json


class TestViews(TestCase):
    """
    Tests for Views.
    """

    def setUp(self):
        """
        Create starting paramaters for view tests with Client, database, and urls.
        """
        self.client = Client()

        self.home_url = reverse('home')
        self.search_url = reverse('search')
        self.results_url = reverse('results')

    def test_HomePage_GET_response(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'swapi_info/home.html')

    def test_HomePage_error_POST_response(self):
        response = self.client.post(self.home_url)

        self.assertEquals(response.status_code, 405)

    def test_HomePage_error_DELETE_response(self):
        response = self.client.delete(self.home_url)

        self.assertEquals(response.status_code, 405)

    def test_search_GET_response(self):
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'swapi_info/search.html')

    def test_search_error_POST_response(self):
        response = self.client.post(self.search_url)

        self.assertEquals(response.status_code, 405)

    def test_results_GET_response(self):
        response = self.client.get(self.results_url, {'search_type': 'films'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'swapi_info/results.html')

    def test_results_POST_response(self):
        response = self.client.post(
            self.results_url, {'search_type': 'planets'})

        self.assertEquals(response.status_code, 405)

    def test_results_DELETE_response(self):
        response = self.client.delete(
            self.results_url, {'search_type': 'starships'})

        self.assertEquals(response.status_code, 405)

    def test_results_invalid_search_response(self):
        response = self.client.get(
            self.results_url, {'search_type': 'bad_test_type'})

        self.assertEquals(response.status_code, 400)

    def test_details_GET_response(self):
        details_url = reverse('details', args=['vehicles', 'AT-AT'])
        response = self.client.get(details_url)

        self.assertEquals(response.status_code, 200)

    def test_details_POST_response(self):
        details_url = reverse('details', args=['vehicles', 'AT-AT'])
        response = self.client.post(details_url)

        self.assertEquals(response.status_code, 405)

    def test_details_DELETE_response(self):
        details_url = reverse('details', args=['vehicles', 'AT-AT'])
        response = self.client.delete(details_url)

        self.assertEquals(response.status_code, 405)

    def test_details_invalid_search_type_response(self):
        details_url = reverse('details', args=['bad_search_type', 'AT-AT'])
        response = self.client.get(details_url)

        self.assertEquals(response.status_code, 400)

    def test_detials_invalid_search_name_response(self):
        details_url = reverse(
            'details', args=['vehicles', 'Bad vehicle name'])
        response = self.client.get(details_url)

        self.assertEquals(response.status_code, 400)

    def test_favorite_valid_post_response(self):
        favorite_url = reverse('favorite', args=['planets', 'Naboo'])
        response = self.client.post(
            favorite_url, {'item_type': 'planets', 'item_name': 'Naboo'})

        self.assertEquals(response.status_code, 201)

    def test_favorite_get_response(self):
        favorite_url = reverse('favorite', args=['planets', 'Naboo'])
        response = self.client.get(
            favorite_url, {'item_type': 'planets', 'item_name': 'Naboo'})

        self.assertEquals(response.status_code, 405)

    def test_favorite_delete_response(self):
        favorite_url = reverse('favorite', args=['planets', 'Naboo'])
        response = self.client.delete(
            favorite_url, {'item_type': 'planets', 'item_name': 'Naboo'})

        self.assertEquals(response.status_code, 405)

    def test_favorite_invalid_item_type_post_response(self):
        favorite_url = reverse('favorite', args=['bad_item_type', 'Naboo'])
        response = self.client.post(
            favorite_url, {'item_type': 'bad_item_type', 'item_name': 'Naboo'})

        self.assertEquals(response.status_code, 400)

    def test_favorite_invalid_item_name_post_response(self):
        favorite_url = reverse(
            'favorite', args=['planets', 'Not a planet Name'])
        response = self.client.post(
            favorite_url, {'item_type': 'planets', 'item_name': 'Not a planet Name'})

        self.assertEquals(response.status_code, 400)
