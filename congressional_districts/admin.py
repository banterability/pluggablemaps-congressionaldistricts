# Admin
from django.contrib.gis import admin

# Models
from congressional_districts.models import District

class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ('display_name', 'district_number', 'state', 'at_large')
    list_filter = ('state', 'at_large')
    search_fields = ('ordinal_name', 'state', 'district_number',)
    fieldsets = (
        (('Boundaries'),
            {'fields': ('polygon_4269', ),
             'classes': ('wide',),
            }
        ),
        (('Description'),
           {'fields': (
                'district_number', 'ordinal_name', 'name', 'lsad', 
                  'lsad_trans', 'state', 'slug', 'square_miles', 'at_large'),
            'classes': ('wide',),
           }
        ),
        (('ID Codes'),
           {'fields': (
                'state_fips_code',),
            'classes': ('wide',),
           }
        ),
     )
    readonly_fields = (
        'district_number', 'ordinal_name',
        'name', 'lsad', 'lsad_trans',
        'state', 'slug', 'square_miles', 'at_large',
        'state_fips_code'
        )
    layerswitcher = False
    scrollable = False
    map_width = 400
    map_height = 400
    modifiable = False

admin.site.register(District, DistrictAdmin)



