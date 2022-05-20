from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Ride, Profile, Bike
from haversine import haversine, Unit


class PositionSerializer(serializers.Serializer):
    lat = serializers.IntegerField()
    lon = serializers.IntegerField()


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fields = ['status', 'start_location_lat', 'start_location_lon', 'end_location_lat',
                            'end_location_lon']

    def create(self, validated_data):
        profile = Profile.objects.get(user__id=validated_data.get('rider'))
        bike = Bike.objects.get(id=validated_data.get('bike'))
        ride = Ride(bike=bike, rider=profile.user, start_location_lat=bike.location_lat,
                    start_location_lon=bike.location_lon)

        if haversine((profile.location_lat, profile.location_lon),
                     (bike.location_lat, bike.location_lon), unit=Unit.METERS) > 100:
            raise serializers.ValidationError(detail='too long distance between rider and bike')

        if profile.status == 'BUSY':
            raise serializers.ValidationError(detail='rider is not available')

        if bike.status == 'BUSY':
            raise serializers.ValidationError(detail='bike is not available')

        bike.status = 'BUSY'
        bike.save()
        profile.status = 'BUSY'
        profile.save()

        return ride


def finish_ride(pk, lat, lon):
    try:
        ride = Ride.objects.get(id=pk)
    except:
        raise serializers.ValidationError(detail='ride does not exist')
    if ride.status == 'FINISHED':
        raise serializers.ValidationError(detail='ride is finished')
    ride.rider.profile.status = 'AVAILABLE'
    ride.rider.profile.save()
    ride.bike.status = 'AVAILABLE'
    ride.bike.location_lat = lat
    ride.bike.location_lon = lon
    ride.bike.save()
    ride.end_location_lat = lat
    ride.end_location_lon = lon
    ride.status = 'FINISHED'
    ride.save()
