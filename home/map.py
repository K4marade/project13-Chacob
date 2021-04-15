import folium


class OpenStreetMap:

    def __init__(self):
        pass

    @staticmethod
    def display_map(lat, lng, zoom, address):
        osmap = folium.Map(location=[lat, lng], zoom_start=zoom)
        layer = folium.raster_layers
        layer.TileLayer(detect_retina=True).add_to(osmap)
        layer.TileLayer('Stamen Terrain', name='Terrain', detect_retina=True).add_to(osmap)
        folium.LayerControl().add_to(osmap)

        folium.Marker([lat, lng], popup=address).add_to(osmap)

        osmap = osmap._repr_html_()

        return osmap

