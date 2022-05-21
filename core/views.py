# Create your views here.
import json

import requests
from django.db.transaction import atomic
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Ride
from .serializers import RideSerializer, PositionSerializer, finish_ride, RegisterSerializer, UserSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


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

    @atomic
    @action(detail=True, methods=['post'], serializer_class=PositionSerializer)
    def finish_ride(self, request, pk=None):
        position_serializer = PositionSerializer(data=request.data)
        if position_serializer.is_valid():
            ride = finish_ride(pk, **position_serializer.data)

            # request to another server to create the receipt of this ride and calculate the desired things:
            r = requests.post('http://127.0.0.1:8003/api/scoring/receipt/',
                              data=json.dumps({
                                  "distance": int(ride.get_distance()),
                                  "user_id": int(ride.rider.id),
                              }),
                              headers={
                                  'content-type': 'application/json',
                              })
            if r.status_code == 200:
                return Response({'message': 'ok'}, status.HTTP_200_OK)
            else:
                return Response({'message': 'error in creating receipt'}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'wrong data'}, status.HTTP_400_BAD_REQUEST)
