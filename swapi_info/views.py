from django.shortcuts import render
import swapi
import requests
import json
from .forms import SearchForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import caches
from django.core import serializers
from django.views.generic import ListView
from django.template.response import TemplateResponse
# from django.views.decorators.cache import cache_page


def home(request):
    return render(request, "swapi_info/home.html")


def search(request):
    form = SearchForm()

    return render(request, 'swapi_info/search.html', {'form': form})


class ResultList(ListView):
    template_name = 'results.html'

    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            search_type = form.cleaned_data['search_type']
            context = {'search_type': search_type, 'result': []}

            if search_type in caches['default']:
                context['result'] = caches['default'].get(search_type)
                return TemplateResponse(request, 'swapi_info/result.html', context, status=200)
            else:
                swapi_json_data = requests.get(
                    'http://swapi.co/api/' + search_type + '/')
                swapi_data = json.loads(json.dumps(swapi_json_data.json()))

                while swapi_data['next'] != None:
                    for item in swapi_data['results']:
                        context['result'].append(item)
                    swapi_json_data = requests.get(swapi_data['next'])
                    swapi_data = json.loads(
                        json.dumps(swapi_json_data.json()))
                else:
                    for item in swapi_data['results']:
                        context['result'].append(item)
                caches['default'].add(search_type, context['result'])
                return TemplateResponse(request, 'swapi_info/result.html', context, status=200)

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
