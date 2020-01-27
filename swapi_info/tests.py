from django.test import TestCase
from django.urls import reverse, resolve
from swapi_info.views import HomePage, search, ResultList, ItemDetails, add_favorite


class TestUrls (TestCase):
    """
    Tests that all URL endpoints resolve.
    """

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePage)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_results_url_is_resolved(self):
        url = reverse('results')
        self.assertEquals(resolve(url).func.view_class, ResultList)

    def test_details_url_is_resolved(self):
        url = reverse('details', args=['test_type', 'test_name'])
        self.assertEquals(resolve(url).func.view_class, ItemDetails)

    def test_favorite_url_is_resolved(self):
        url = reverse('favorite', args=['test_type', 'test_name'])
        self.assertEquals(resolve(url).func, add_favorite)
