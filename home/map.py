import folium
import geocoder
import requests


class OpenStreetMap:
    """Class that defines a map to be displayed to the user"""

    def __init__(self):
        """Class constructor"""
        self.lat = []
        self.lng = []
        self.address = []

    def get_places_location(self, search):
        url = "https://nominatim.openstreetmap.org/search"

        params = {
            "amenity": 'veterinaire',
            "city": search,
            "country": "france",
            "countrycodes": "fr",
            "limit": 100,
            "addressdetails": "1",
            "format": "json"
        }

        data = requests.get(url, params)
        response = data.json()

        for place in response:
            address = place['address']
            city = address.get("city_district") or address.get("municipality")
            if search in city or search in address.get("postcode"):
                self.lat.append(place["lat"])
                self.lng.append(place["lon"])
                complete_address = f"{address.get('amenity', 'Vétérinaire')}\n{address.get('road')}\n" \
                                   f"{address.get('postcode')} {city}"
                self.address.append(complete_address)
        return self.lat, self.lng, self.address

    @staticmethod
    def display_map(places, city):
        """Method that return a map in an html representation
        to be displayed to the user in a template"""

        # Get city coordinates
        city = geocoder.osm(location=city + ", FR", )

        # Initialise map
        osmap = folium.Map(location=[city.lat, city.lng], zoom_start=11)

        # Add layers
        layer = folium.raster_layers
        layer.TileLayer(detect_retina=True).add_to(osmap)
        layer.TileLayer('Stamen Terrain', name='Terrain', detect_retina=True).add_to(osmap)
        folium.LayerControl().add_to(osmap)

        # Add markers according to results from search
        for lat, lng, address in zip(places[0], places[1], places[2]):  # (self.lat, self.lng, self.address):
            folium.Marker(location=[lat, lng], popup=address).add_to(osmap)

        # Render map with html code
        osmap = osmap._repr_html_()

        return osmap
