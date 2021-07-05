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
            "q": "Clinique Vétérinaire, Vétérinaire, " + search + ", FR",
            "limit": 20,
            "country": "france",
            "countrycodes": "fr",
            "addressdetails": "1",
            "format": "json"
        }

        data = requests.get(url, params)
        response = data.json()

        for place in response:
            address = place['address']
            if search in address["municipality"] or search in address["postcode"]:
                self.lat.append(place["lat"])
                self.lng.append(place["lon"])
                # address = place['address']
                complete_address = address['amenity'] + "\n" + address['road'] + "\n" + address['postcode'] + " "\
                    + address['municipality']
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
