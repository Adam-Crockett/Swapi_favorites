from django import forms
from django.conf import settings
import requests


class SearchForm(forms.Form):
    type_choices = [('films', 'Films'), ('people', 'People'), ('species', 'Species'), ('planets', 'Planets'),
                    ('starships', 'Starships'), ('vehicles', 'Vehicles')]
    search_type = forms.CharField(
        label='Search Type', widget=forms.Select(choices=type_choices))
    # name = forms.CharField(label='name', max_length=100)
