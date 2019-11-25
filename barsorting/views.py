from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BarValues

# Create your views here.


def sorting(request):
    new_bars = BarValues()
    context = {
        'bar_values': new_bars.get_bar_values,
    }
    return render(request, 'barsorting/sorting.html', context)
