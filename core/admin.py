from django.contrib import admin

from .models import Bike, Ride, Profile

admin.site.register(Ride)
admin.site.register(Profile)
admin.site.register(Bike)
