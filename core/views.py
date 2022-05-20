# Create your views here.
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Ride
from .serializers import RideSerializer
from drf_yasg.utils import swagger_auto_schema


class RideViewSet(ModelViewSet):
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]
    queryset = Ride.objects.all()

    def create(self, request, *args, **kwargs):
        ride_serializer = RideSerializer(data=request.data)
        if ride_serializer.is_valid():
            ride = ride_serializer.create(validated_data=request.data)
            ride.save()
            return Response({'message': 'ok'}, status.HTTP_200_OK)
        else:
            return Response({'message': 'wrong data'}, status.HTTP_400_BAD_REQUEST)


@action(detail=True, methods=['post'])
def finish_ride(self, request, pk=None):
    print(pk)
    content = {
        'status': 'request was permitted'
    }
    return Response(content)
