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
