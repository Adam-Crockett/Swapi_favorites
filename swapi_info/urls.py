from django.urls import path
from . import views
from swapi_info.views import ResultList, ItemDetails

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('results/', ResultList.as_view(), name='results'),
    path('details/<str:search_type>/<str:name>/',
         ItemDetails.as_view(), name='details'),
]
