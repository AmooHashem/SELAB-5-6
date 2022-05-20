from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class RideView(APIView):
    permission_classes = [IsAuthenticated]

    def start_ride(self, request):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    def finish_ride(self, request):
        return Response("salam")
