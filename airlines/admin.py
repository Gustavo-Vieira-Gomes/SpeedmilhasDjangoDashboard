from django.contrib import admin
from airlines.models import Airline


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
