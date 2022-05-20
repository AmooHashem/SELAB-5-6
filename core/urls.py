from django.urls import path

from .views import start_ride, finish_ride

urlpatterns = [
    path('start_ride', start_ride, name='start ride'),
    path('finish_ride', finish_ride, name='finish ride'),
]
