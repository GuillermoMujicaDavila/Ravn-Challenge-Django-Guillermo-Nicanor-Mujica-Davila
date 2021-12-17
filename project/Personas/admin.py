from typing import List
from django.contrib import admin
from .models import PersonModel, VehiclesModel

class PersonAdmin (admin.ModelAdmin):
    list_display = ['personId', 'personName', 'personEye', 'personHair', 'personSkin','personBirth','personType','personHouse']

    search_fields = ['personName']

    readonly_fields = ['personId']
    
class VehicicleAdmin (admin.ModelAdmin):
    list_display = ['vehiclesId', 'vehiclesName', 'personID']
    
    search_fields = ['vehiclesName']

    readonly_fields = ['vehiclesId']

admin.site.register(PersonModel,PersonAdmin)
admin.site.register(VehiclesModel,VehicicleAdmin)
# Register your models here.
