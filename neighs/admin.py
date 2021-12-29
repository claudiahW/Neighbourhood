from django.contrib import admin
from .models import NeighborHood,Profile,Location

# Register your models here.
admin.site.register(Profile)
admin.site.register(NeighborHood)
admin.site.register(Location)
