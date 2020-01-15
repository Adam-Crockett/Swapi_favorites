from django.urls import path
from . import views
from swapi_info.views import ResultList, ItemDetails, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('search', views.search, name='search'),
    path('results/', ResultList.as_view(), name='results'),
    path('details/<str:search_type>/<str:name>/',
         ItemDetails.as_view(), name='details'),
    path('details/<str:search_type>/<str:name>/favorite',
         views.add_favorite, name='favorite'),
]
