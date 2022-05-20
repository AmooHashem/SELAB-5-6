# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def start_ride(request):
    user = request.user
    print(user)
    content = {
        'status': 'request was permitted'
    }
    return Response(content)


@api_view(['POST'])
def finish_ride(request):
    return Response("salam")
