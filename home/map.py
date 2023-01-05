import folium
import geocoder
import requests
from django.conf import settings
from folium import TileLayer
from folium.plugins import MarkerCluster, LocateControl

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
                complete_address = f"{address.get('amenity', 'Vétérinaire')}<br/>{address.get('road')}<br/>" \
                                   f"{address.get('postcode')} {city}"
                self.address.append(complete_address)
        return self.lat, self.lng, self.address

    @staticmethod
    def display_map(places, city):
        """Method that return a map in an html representation
        to be displayed to the user in a template"""

        # Get city coordinates
        city = geocoder.osm(location=f"{city}, FR")

        # Initialise map
        osmap = folium.Map(location=[city.lat, city.lng], zoom_start=11)

        # Add markers
        markers = [
            [lat, lng, address] for lat, lng, address in zip(places[0], places[1], places[2])
        ]

        # Set cluster with markers
        marker_cluster = MarkerCluster(
            name="Vet Markers",
            control=False,
            options={"showCoverageOnHover": False,}
        ).add_to(osmap)

        for marker in markers:
            lat = marker[0]
            lng = marker[1]
            # Remove `</br>` element from addresses
            clean_address = marker[2].replace('<br/>', ' ')

            url = f"<a href='https://www.google.com/maps/search/{clean_address}/@{lat},{lng}z' target='_blank'>{marker[2]}</a>"
            folium.Marker(
                location=[marker[0], marker[1]],
                popup=folium.Popup(html=url, max_width=150),
                icon=folium.map.Icon(color="blue", prefix="fa", icon="fa-solid fa-house-medical"),
            ).add_to(marker_cluster)


        # Geolocation
        location = LocateControl()
        location.options = {
            "flyTo": True,
            "icon": "fa-solid fa-location-arrow",
        }
        location.add_to(osmap)

        # Mapbox Layer
        tile_url = f'https://api.mapbox.com/styles/v1/mapbox/streets-v12/tiles/256/{{z}}/{{x}}/{{y}}?access_token={settings.MAPBOX_KEY}'
        layer = TileLayer(
            tiles=tile_url,
            attr="Mapbox©",
            name="Mapbox",
            detect_retina=True,
        )
        layer.add_to(osmap)

        # Render map with html code
        osmap = osmap._repr_html_()

        return osmap
