from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import caches
from django.core import serializers
from django.views.generic import ListView, DetailView
from django.template.response import TemplateResponse
from swapi_info.handlers import CacheController, DetailGathering


def home(request):
    return render(request, "swapi_info/home.html")


def search(request):
    form = SearchForm()

    return render(request, 'swapi_info/search.html', {'form': form})


class ResultList(ListView):

    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            search_type = form.cleaned_data['search_type']
            context = {'search_type': search_type, 'item_list': []}
            cache_control = CacheController()
            context['item_list'] = cache_control.get_cache(search_type)

            return TemplateResponse(request, 'swapi_info/results.html', context, status=200)


class ItemDetails(DetailView):

    def get(self, request, search_type, name):
        cache_control = CacheController()
        detail_gatherer = DetailGathering()
        context = {'search_type': search_type, 'result_name': name}
        item_list = cache_control.get_cache(search_type)
        type_handler = {
            'item': [detail_gatherer.item_handler],
            'films': [detail_gatherer.film_handler, 'swapi_info/film_details.html'],
            'people': [detail_gatherer.people_handler, 'swapi_info/person_details.html'],
            'species': [detail_gatherer.species_handler, 'swapi_info/species_details.html'],
            'planets': [detail_gatherer.planet_handler, 'swapi_info/planet_details.html'],
            'starships': [detail_gatherer.starship_handler, 'swapi_info/starship_details.html'],
            'vehicles': [detail_gatherer.vehicle_handler, 'swapi_info/vehicle_details.html']}

        item = type_handler['item'][0](
            item_list, search_type, name)
        context['item'] = item

        context = type_handler[search_type][0](item)

        return TemplateResponse(request, type_handler[search_type][1], context, status=200)

    # def item_handler(self, item_list, search_type, name):
    #     if search_type != 'films':
    #         for item in item_list:
    #             if item['name'] == name:
    #                 return item
    #     else:
    #         for item in item_list:
    #             if item['title'] == name:
    #                 return item
    #     return HttpResponse(status=406)

    # def film_handler(self, request, film):
    #     characters = []
    #     species = []
    #     planets = []
    #     starships = []
    #     vehicles = []
    #     # films = []

    #     producer = film['producer'].split(',')

    #     # for film in self.cache_control.get_cache('films'):
    #     #     if film['url'] in item['films']:
    #     #         films.append(film['title'])

    #     # return films

    #     for person in self.cache_control.get_cache('people'):
    #         if person['url'] in film['characters']:
    #             characters.append(person['name'])

    #     for specie in self.cache_control.get_cache('species'):
    #         if specie['url'] in film['species']:
    #             species.append(specie['name'])

    #     for planet in self.cache_control.get_cache('planets'):
    #         if planet['url'] in film['planets']:
    #             planets.append(planet['name'])

    #     for starship in self.cache_control.get_cache('starships'):
    #         if starship['url'] in film['starships']:
    #             starships.append(starship['name'])

    #     for vehicle in self.cache_control.get_cache('vehicles'):
    #         if vehicle['url'] in film['vehicles']:
    #             vehicles.append(vehicle['name'])

    #     context = {'item': film, 'producer': producer, 'characters': characters, 'planets': planets,
    #                'species': species, 'starships': starships, 'vehicles': vehicles}

    #     return TemplateResponse(request, 'swapi_info/film_details.html', context, status=200)

    # def people_handler(self, person):
    #     pass

    # def species_handler(self, species):
    #     pass

    # def planet_handler(self, planet):
    #     pass

    # def starship_handler(self, starship):
    #     pass

    # def vehicle_handler(self, vehicle):
    #     pass

        # def get_queryset(self, request):
        #     if request.method == 'GET':
        #         form = SearchForm(request.GET)
        #         if form.is_valid():
        #             # process the data in form.cleaned_data as required
        #             result = []
        #             search_type = form.cleaned_data['search_type']

        #             if search_type in caches['default']:
        #                 result = caches['default'].get(search_type)
        #                 return result
        #             else:
        #                 swapi_json_data = requests.get(
        #                     'http://swapi.co/api/' + search_type + '/')
        #                 swapi_data = json.loads(json.dumps(swapi_json_data.json()))

        #                 while swapi_data['next'] != None:
        #                     for obj in swapi_data['results']:
        #                         result.append(obj)
        #                     swapi_json_data = requests.get(swapi_data['next'])
        #                     swapi_data = json.loads(
        #                         json.dumps(swapi_json_data.json()))
        #                 else:
        #                     for obj in swapi_data['results']:
        #                         result.append(obj)
        #                 caches['default'].add(search_type, result)
        #                 return result

        # def result(request):

        #     if request.method == 'GET':
        #         # create a form instance and populate it with data from the request:
        #         form = SearchForm(request.GET)
        #         # check whether it's valid:
        #         if form.is_valid():
        #             # process the data in form.cleaned_data as required
        #             context = {}
        #             result = []
        #             search_type = form.cleaned_data['search_type']

        #             if search_type in caches['default']:
        #                 result = caches['default'].get(search_type)
        #             else:
        #                 swapi_json_data = requests.get(
        #                     'http://swapi.co/api/' + search_type + '/')
        #                 swapi_data = json.loads(json.dumps(swapi_json_data.json()))

        #                 while swapi_data['next'] != None:
        #                     for obj in swapi_data['results']:
        #                         result.append(obj)
        #                     swapi_json_data = requests.get(swapi_data['next'])
        #                     swapi_data = json.loads(json.dumps(swapi_json_data.json()))
        #                 else:
        #                     for obj in swapi_data['results']:
        #                         result.append(obj)
        #                 caches['default'].add(search_type, result)

        #             context['search_type'] = search_type
        #             context['search_set'] = result

        #             # Send to list result page
        #             return render(request, 'swapi_info/result.html', context)

        #     # if a GET (or any other method) we'll create a blank form
        #     else:
        #         return render(request, "swapi_info/search.html")
