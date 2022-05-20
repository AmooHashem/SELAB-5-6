# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def start_ride(self, request):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)


@api_view()
def finish_ride(self, request):
    return Response("salam")
