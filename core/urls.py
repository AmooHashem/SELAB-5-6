from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RideViewSet, RegisterApi

router = DefaultRouter()

urlpatterns = [
    path('register_user', RegisterApi.as_view(), name='register'),
]

router.register('ride', RideViewSet, basename='ride')

urlpatterns += router.urls
