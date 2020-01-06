from django.shortcuts import render
import swapi
from .forms import SearchForm
from django.http import HttpResponseRedirect
from django.core.cache import caches
from django.core.cache import cache
from django.views.decorators.cache import cache_page


def home(request):
    return render(request, "swapi_info/home.html")


def search(request):
    form = SearchForm()

    return render(request, 'swapi_info/search.html', {'form': form})


@cache_page(60 * 15)
def result(request):

    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            context = {}
            search_type = form.cleaned_data['search_type']
            name = form.cleaned_data['name'].title()
            search_result = None
            search_collection = []

            # num_results = swapi.get_all(search_type).count()

            if search_type in caches['default']:
                search_set = caches['default'].get(search_type)
            else:
                request_search_set = swapi.get_all(search_type)
                caches['default'].add(search_type, request_search_set)
                search_set = caches['default'].get(search_type)

            if search_type == "films":
                for item in search_set.iter():
                    if item.title == name:
                        search_result = item
                        break
            else:
                for item in search_set.iter():
                    search_collection.append(item)
                    if item.name == name:
                        search_result = item

            context.update({'search_type': search_type})
            # context.update({'num_results': num_results})
            context.update({'search_result': search_result})
            context.update({'search_collection': search_collection})
            context.update({'name': name})

            # redirect to a new URL:
            return render(request, 'swapi_info/result.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, "swapi_info/search.html")
