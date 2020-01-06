from django.apps import AppConfig
from django.core.cache import caches
import swapi


class SwapiInfoConfig(AppConfig):
    name = 'swapi_info'

    def ready(self):
        caches['default'].add('films', swapi.get_all('films'))
        caches['default'].add('people', swapi.get_all('people'))
        caches['default'].add('species', swapi.get_all('species'))
        caches['default'].add('planets', swapi.get_all('planets'))
        caches['default'].add('starships', swapi.get_all('starships'))
        caches['default'].add('vehicles', swapi.get_all('vehicles'))
