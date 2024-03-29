from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django_google_maps.models import Dentstudio

class DentstudioAdmin(admin.ModelAdmin):
    formfield_overrides = { 
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget}, } 

admin.site.register(Dentstudio, DentstudioAdmin)		