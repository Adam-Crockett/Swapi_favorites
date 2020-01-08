from django.shortcuts import render
import swapi
import requests
import json
from .forms import SearchForm
from django.http import HttpResponseRedirect
from django.core.cache import caches
from django.core.cache import cache
from django.core import serializers
# from django.views.decorators.cache import cache_page


def home(request):
    return render(request, "swapi_info/home.html")


def search(request):
    form = SearchForm()

    return render(request, 'swapi_info/search.html', {'form': form})


# @cache_page(60 * 15)
def result(request):

    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            context = {}
            result = []
            search_type = form.cleaned_data['search_type']

            if search_type in caches['default']:
                result = caches['default'].get(search_type)
            else:
                swapi_json_data = requests.get(
                    'http://swapi.co/api/' + search_type + '/')
                swapi_data = json.loads(json.dumps(swapi_json_data.json()))

                while swapi_data['next'] != None:
                    for obj in swapi_data['results']:
                        result.append(obj)
                    swapi_json_data = requests.get(swapi_data['next'])
                    swapi_data = json.loads(json.dumps(swapi_json_data.json()))
                else:
                    for obj in swapi_data['results']:
                        result.append(obj)
                caches['default'].add(search_type, result)

            context['search_type'] = search_type
            context['search_set'] = result

            # Send to list result page
            return render(request, 'swapi_info/result.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "swapi_info/search.html")
