from django.shortcuts import render
from django.contrib import messages
import folium
import geocoder


def home_view(request):
    """
    Display the home page

     **Template:**
    :template:`home.html`
    """

    # Create Map object
    osm_map = folium.Map(location=[48.8534, 2.3488], zoom_start=5)
    layer = folium.raster_layers
    layer.TileLayer(detect_retina=True).add_to(osm_map)
    layer.TileLayer('Stamen Terrain', name='Terrain', detect_retina=True).add_to(osm_map)
    folium.LayerControl().add_to(osm_map)

    search_address = request.POST.get('search-address')
    if search_address:
        location = geocoder.osm(search_address)
        lat = location.lat
        lng = location.lng
        country = location.country
        if lat is None or lng is None:
            message = messages.error(
                request, "Nous n'avons pas pu trouver de résultat. Réessayez")
            return render(request, 'home.html', locals())
        else:
            osm_map = folium.Map(location=[lat, lng], zoom_start=17)

            # Put Marker on the map
            folium.Marker([lat, lng], popup=country).add_to(osm_map)
            layer = folium.raster_layers
            layer.TileLayer(detect_retina=True).add_to(osm_map)
            layer.TileLayer('Stamen Terrain', name='Terrain', detect_retina=True).add_to(osm_map)
            folium.LayerControl().add_to(osm_map)
    else:
        pass

    # Represents the maps as html code
    osm_map = osm_map._repr_html_()

    return render(request, 'home.html', {'osm_map': osm_map})


def legal_view(request):
    """
    Display the legal page

     **Template:**
    :template:`legal.html`
    """

    return render(request, 'legal.html')
