from django import forms
from django.conf import settings
import requests
from swapi_info import static


class SearchForm(forms.Form):
    """
    Search form used on the search page of site. Lets the user select the type of Search to run.
    """

    type_choices = [('films', 'Films'), ('people', 'People'), ('species', 'Species'), ('planets', 'Planets'),
                    ('starships', 'Starships'), ('vehicles', 'Vehicles')]
    # search_type = forms.CharField(widget=forms.Select(
    #     choices=type_choices))

    search_type = forms.CharField(
        widget=forms.RadioSelect(choices=type_choices))
