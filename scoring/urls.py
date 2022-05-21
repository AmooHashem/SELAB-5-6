from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ReceiptApiView

router = DefaultRouter()

urlpatterns = []

router.register('receipt', ReceiptApiView, basename='receipt')

urlpatterns += router.urls
