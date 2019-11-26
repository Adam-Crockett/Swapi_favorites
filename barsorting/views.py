from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BarValues

# Create your views here.


# def sorting_page(request):
#     bar_set = BarValues()
#     context = {
#         'bar_set': bar_set.get_bar_values,
#     }
#     return render(request, 'barsorting/sorting.html', context)

def reset_bars(request):
    bar_set = BarValues()
    context = {
        'bar_set': bar_set.get_bar_values,
    }
    return render(request, 'barsorting/sorting.html', context)
