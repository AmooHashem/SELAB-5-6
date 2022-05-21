from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from haversine import haversine, Unit


class Profile(models.Model):
    STATUS = (
        ("AVAILABLE", "Available"),
        ("BUSY", "Busy")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location_lat = models.FloatField(default=0)
    location_lon = models.FloatField(default=0)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="AVAILABLE")

    def __str__(self):
        return f'{self.user.id}-{self.user.username}'


class Bike(models.Model):
    STATUS = (
        ("AVAILABLE", "Available"),
        ("BUSY", "Busy")
    )
    name = models.CharField(max_length=20, blank=True, null=True)
    location_lat = models.FloatField(default=0)
    location_lon = models.FloatField(default=0)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="AVAILABLE")

    def __str__(self):
        return f'{self.id}-{self.name}'


class Ride(models.Model):
    STATUS = (
        ("ON_GOING", "on-going"),
        ("FINISHED", "Finished")
    )
    bike = models.ForeignKey(to=Bike, on_delete=models.CASCADE)
    rider = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="ON_GOING")
    start_location_lat = models.FloatField(blank=True, null=True)
    start_location_lon = models.FloatField(blank=True, null=True)
    end_location_lat = models.FloatField(blank=True, null=True)
    end_location_lon = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'id: {self.id} - rider: {self.rider} - bike: {self.bike}'

    def get_distance(self):
        if not self.start_location_lat or not self.start_location_lon or \
                not self.end_location_lat or not self.end_location_lon:
            return
        else:
            return haversine((self.start_location_lat, self.start_location_lon),
                             (self.end_location_lat, self.end_location_lon), unit=Unit.METERS)
