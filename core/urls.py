from django.urls import path

from .views import RideView

urlpatterns = [
    path('start_ride', RideView.start_ride, name='start ride'),
    path('finish_ride', RideView.finish_ride, name='finish ride'),
]
