from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RideViewSet

router = DefaultRouter()
urlpatterns = []
router.register('ride', RideViewSet, basename='ride')

urlpatterns += router.urls
