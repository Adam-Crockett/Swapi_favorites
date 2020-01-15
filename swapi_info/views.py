from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import caches
from django.core import serializers
from django.views.generic import ListView, DetailView
from django.template.response import TemplateResponse
from swapi_info.handlers import CacheController, DetailGathering
from swapi_info.models import Favorites


def search(request):
    form = SearchForm()

    return render(request, 'swapi_info/search.html', {'form': form})


class HomePage(ListView):
    template_name = 'swapi_info/home.html'
    context_object_name = 'top_five'
    model = Favorites

    def get_queryset(self):

        item_types = ['films', 'people', 'species',
                      'planets', 'starships', 'vehicles']

        top_five = {
            'films': [],
            'people': [],
            'species': [],
            'planets': [],
            'starships': [],
            'vehicles': []
        }

        for kind in item_types:
            top_five_qs = Favorites.objects.filter(
                item_type=kind).order_by('-favorite_count')[:5]
            for item in top_five_qs:
                top_five[kind].append(
                    [item.name, item.favorite_count])

        return top_five


class ResultList(ListView):

    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            search_type = form.cleaned_data['search_type']
            context = {'search_type': search_type,
                       'item_list': [], 'form': form}
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

        context['item_content'] = type_handler[search_type][0](item)

        return TemplateResponse(request, type_handler[search_type][1], context, status=200)


def add_favorite(request, *args, **kwargs):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        item_type = request.POST['item_type']
        swapi_url = request.POST['item_url']

        obj, created = Favorites.objects.get_or_create(
            name=item_name, item_type=item_type, swapi_url=swapi_url, defaults={'favorite_count': 1})

        if not created:
            obj.favorite_count += 1
            obj.save()

        return TemplateResponse(request, 'swapi_info/favorite_added.html', status=201)

    else:
        return HttpResponse(status=404)
