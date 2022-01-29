from django.shortcuts import render
from django.contrib import messages

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
        search_address = search_address.capitalize()
        try:
            location = osmap.get_places_location(search_address)
            osmap = osmap.display_map(location, search_address)
        except (IndexError, ValueError, TypeError):
            message = messages.error(
                request, "Nous n'avons pas pu trouver de résultat. Réessayez")
            return render(request, 'home.html', locals())

    return render(request, 'home.html', {'osmap': osmap})


def legal_view(request):
    """
    Display the legal page

     **Template:**
    :template:`legal.html`
    """

    return render(request, 'legal.html')
