import requests
import json
from django.core.cache import caches
from django.http import HttpResponseRedirect, HttpResponse


class CacheController():

    def set_cache(self, search_type):
        data_set = {'item_list': []}
        swapi_json_data = requests.get(
            'http://swapi.co/api/' + search_type + '/')
        swapi_data = json.loads(json.dumps(swapi_json_data.json()))

        while swapi_data['next'] != None:
            for item in swapi_data['results']:
                data_set['item_list'].append(item)

            swapi_json_data = requests.get(swapi_data['next'])
            swapi_data = json.loads(
                json.dumps(swapi_json_data.json()))
        else:
            for item in swapi_data['results']:
                data_set['item_list'].append(item)

        if search_type == 'vehicles':
            data_set['item_list'] = self.handle_bad_name(data_set['item_list'])

        caches['default'].add(search_type, data_set['item_list'])

    def get_cache(self, search_type):
        if search_type in caches['default']:
            return caches['default'].get(search_type)
        else:
            self.set_cache(search_type)
            return caches['default'].get(search_type)

    def handle_bad_name(self, item_list):
        for item in item_list:
            if '/' in item['name']:
                item['name'] = item['name'].replace('/', '-')
        return item_list


class DetailGathering():
    cache_control = CacheController()

    def item_handler(self, item_list, search_type, name):
        if search_type != 'films':
            for item in item_list:
                if item['name'] == name:
                    return item
        else:
            for item in item_list:
                if item['title'] == name:
                    return item
        return HttpResponse(status=406)

    def film_handler(self, film):
        characters = []
        species = []
        planets = []
        starships = []
        vehicles = []

        producer = film['producer'].split(',')

        for person in self.cache_control.get_cache('people'):
            if person['url'] in film['characters']:
                characters.append(person['name'])

        for specie in self.cache_control.get_cache('species'):
            if specie['url'] in film['species']:
                species.append(specie['name'])

        for planet in self.cache_control.get_cache('planets'):
            if planet['url'] in film['planets']:
                planets.append(planet['name'])

        for starship in self.cache_control.get_cache('starships'):
            if starship['url'] in film['starships']:
                starships.append(starship['name'])

        for vehicle in self.cache_control.get_cache('vehicles'):
            if vehicle['url'] in film['vehicles']:
                vehicles.append(vehicle['name'])

        context = {'item': film, 'producer': producer, 'characters': characters, 'planets': planets,
                   'species': species, 'starships': starships, 'vehicles': vehicles}
        return context

    def people_handler(self, person):
        homeworld = []
        films = []
        species = []
        starships = []
        vehicles = []

        for planet in self.cache_control.get_cache('planets'):
            if planet['url'] in person['homeworld']:
                homeworld.append(planet['name'])

        for film in self.cache_control.get_cache('films'):
            if film['url'] in person['films']:
                films.append(film['title'])

        for specie in self.cache_control.get_cache('species'):
            if specie['url'] in person['species']:
                species.append(specie['name'])

        for starship in self.cache_control.get_cache('starships'):
            if starship['url'] in person['starships']:
                starships.append(starship['name'])

        for vehicle in self.cache_control.get_cache('vehicles'):
            if vehicle['url'] in person['vehicles']:
                vehicles.append(vehicle['name'])

        context = {'item': person, 'films': films, 'homeworld': homeworld,
                   'species': species, 'starships': starships, 'vehicles': vehicles}

        return context

    def species_handler(self, species):
        pass

    def planet_handler(self, planet):
        pass

    def starship_handler(self, starship):
        pass

    def vehicle_handler(self, vehicle):
        pass
