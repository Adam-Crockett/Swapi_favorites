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
        # self.details_url = reverse('details', args=['test_type', 'test_name'])
        # self.favorite_url = reverse(
        #     'favorite', args=['test_type', 'test_name'])

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

    def test_HomePage_fail_to_query_top_five(self):
        pass

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
        self.assertTemplateUsed(response, 'swapi_info/400.html')

    def test_results_cache_recall_failure_response(self):
        pass

    def test_details_GET_response(self):
        pass

    def test_details_POST_response(self):
        pass

    def test_details_DELETE_response(self):
        pass

    def test_details_invalid_search_type_response(self):
        pass

    def test_detials_invalid_search_name_response(self):
        pass

    def test_details_cache_recall_failure_response(self):
        pass
