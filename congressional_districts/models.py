from django.contrib.gis.db import models
from django.contrib.localflavor.us.models import USStateField

class District(models.Model):
    state_fips_code = models.CharField(max_length=2)
    cd = models.CharField(max_length=2)
    lsad = models.CharField(max_length=2)
    name = models.CharField(max_length=90)
    lsad_trans = models.CharField(max_length=50)
    
    # generated
    slug = models.SlugField(blank=True, null=True)
    state = USStateField(blank=True, null=True)
    ordinal_name = models.CharField(blank=True, null=True, max_length=50)
    at_large = models.BooleanField(default=False)
    
    # square_miles = models.FloatField(null=True, blank=True)
    # 
    geom = models.MultiPolygonField(srid=4269)
    objects = models.GeoManager()
    
    class Meta:
        verbose_name = "U.S. congressional district"
    
    def __unicode__(self):
        return u"%s: The Fightin' %s" % (self.state, self.ordinal_name)