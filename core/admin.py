from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Escola

admin.site.register(Escola, LeafletGeoAdmin)
"""
class EscolaAdmin(admin.OSMGeoAdmin):

    # Centro do mapa
    # OSMGeoAdmin usa um sistema de projeção diferente de GeoModelAdmin,
    # por isso, a transformação é necessária
    lat, lon = -7.144983, -34.860527 # João Pessoa, PB (Defina as coordenadas da sua cidade)
    pnt = Point(lon, lat, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords

    default_zoom = 12
"""
