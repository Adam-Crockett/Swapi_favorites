from django.shortcuts import render
import requests
import json
from .forms import SearchForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import caches
from django.core import serializers
from django.views.generic import ListView, DetailView
from django.template.response import TemplateResponse


def home(request):
    return render(request, "swapi_info/home.html")


def search(request):
    form = SearchForm()

    return render(request, 'swapi_info/search.html', {'form': form})


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

            # if search_type in caches['default']:
            #     context['item_list'] = caches['default'].get(search_type)
            #     return TemplateResponse(request, 'swapi_info/results.html', context, status=200)
            # else:
            #     swapi_json_data = requests.get(
            #         'http://swapi.co/api/' + search_type + '/')
            #     swapi_data = json.loads(json.dumps(swapi_json_data.json()))

            #     while swapi_data['next'] != None:
            #         for item in swapi_data['results']:
            #             context['item_list'].append(item)
            #         swapi_json_data = requests.get(swapi_data['next'])
            #         swapi_data = json.loads(
            #             json.dumps(swapi_json_data.json()))
            #     else:
            #         for item in swapi_data['results']:
            #             context['item_list'].append(item)
            #     caches['default'].add(search_type, context['item_list'])
            #     return TemplateResponse(request, 'swapi_info/results.html', context, status=200)


class ItemDetails(DetailView):

    def get(self, request, search_type, name):
        context = {'search_type': search_type, 'result_name': name}
        cache_control = CacheController()
        item_list = cache_control.get_cache(search_type)
        type_handler = {
            'item': self.item_handler,
            'films': self.film_handler,
            'people': self.people_handler,
            'species_handler': self.species_handler,
            'planets': self.planet_handler,
            'starships': self.starship_handler,
            'vehicles': self.vehicle_handler}

        item = type_handler['item'](item_list, search_type, name)

        context['item'] = item

        # type_handler[search_type](item)

        return TemplateResponse(request, 'swapi_info/details.html', context, status=200)

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
        pass

    def people_handler(self, person):
        pass

    def species_handler(self, species):
        pass

    def planet_handler(self, planet):
        pass

    def starship_handler(self, starship):
        pass

    def vehicle_handler(self, vehicle):
        pass

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
