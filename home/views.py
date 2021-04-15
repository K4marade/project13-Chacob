from django.shortcuts import render
from django.contrib import messages
import folium
import geocoder
from .map import OpenStreetMap


def home_view(request):
    """
    Display the home page

     **Template:**
    :template:`home.html`
    """

    osmap = OpenStreetMap()
    search_address = request.POST.get('search-address')

    if search_address:
        location = geocoder.osm(search_address)
        lat = location.lat
        lng = location.lng
        address = location.address
        if lat is None or lng is None:
            message = messages.error(
                request, "Nous n'avons pas pu trouver de résultat. Réessayez")
            return render(request, 'home.html', locals())
        else:
            osmap = osmap.display_map(lat, lng, 15, address)  # = folium.Map(location=[lat, lng], zoom_start=17)

    return render(request, 'home.html', {'osmap': osmap})


def legal_view(request):
    """
    Display the legal page

     **Template:**
    :template:`legal.html`
    """

    return render(request, 'legal.html')
