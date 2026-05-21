from django.contrib import admin

from apps.aircraft.models.aircraft import Aircraft
from apps.aircraft.models.aircraft_type import AircraftType
from apps.aircraft.models.operator import Operator

admin.site.register(Aircraft)
admin.site.register(AircraftType)
admin.site.register(Operator)
