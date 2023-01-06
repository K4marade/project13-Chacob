from home.map import OpenStreetMap


class TestMapLocations:
    """Class that tests OSM locations"""

    def setup_class(self):
        self.map = OpenStreetMap()

    def test_get_places_location(self, monkeypatch):
        places = ([48.8534, 45.764043],
                  [2.3488, 4.835659],
                  ['Vétérinaire<br/>''rue de Lyon<br/>''75012 Paris',
                   'Vétérinaire<br/>''Avenue du Maine<br/>''75014 Paris'],)

        class MockRequestResponse:
            status_code = 200

            @staticmethod
            def json():
                return [
                    {
                        "lat": 48.8534,
                        "lon": 2.3488,
                        "address": {
                            "municipality": "Paris",
                            "amenity": "Vétérinaire",
                            "road": "rue de Lyon",
                            "postcode": "75012"
                        }
                    },
                    {
                        "lat": 45.764043,
                        "lon": 4.835659,
                        "address": {
                            "municipality": "Paris",
                            "amenity": "Vétérinaire",
                            "road": "Avenue du Maine",
                            "postcode": "75014"
                        }
                    }
                ]

        def mockreturn(*args):
            mockreturn.params = {"args": args}
            response = MockRequestResponse
            return response

        monkeypatch.setattr("requests.get", mockreturn)

        assert self.map.get_places_location("Paris") == places

        assert MockRequestResponse.status_code == 200
