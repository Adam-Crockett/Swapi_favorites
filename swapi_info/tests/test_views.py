from django.test import TestCase
from django.urls import reverse
from swapi_info.views import HomePage, search, ResultList, ItemDetails, add_favorite


class TestViews(TestCase):
    """
    Tests for Views.
    """

    def setUp(self):
        """
        Create starting paramaters for view tests with Client, database, and urls.
        """

    def test_HomePage_GET_response(self):
        pass

    def test_HomePage_error_POST_response(self):
        pass

    def test_HomePage_error_DELETE_response(self):
        pass

    def test_search_GET_response(self):
        pass

    def test_search_error_POST_response(self):
        pass
