# Admin
from django.contrib.gis import admin

# Models
from congressional_districts.models import District

class DistrictAdmin(admin.OSMGeoAdmin):
    pass

admin.site.register(District, DistrictAdmin)
