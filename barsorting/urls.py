from django.urls import path

from . import views

urlpatterns = [
    path('', views.reset_bars, name='sorting'),
    path('reset', views.reset_bars, name='sorting')
]
