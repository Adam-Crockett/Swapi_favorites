from django.urls import path
from . import views
from swapi_info.views import ResultList

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('result/', ResultList.as_view(), name='result'),
    # path('detials', views.result, name='details'),
]
