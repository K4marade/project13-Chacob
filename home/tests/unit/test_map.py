from home.map import OpenStreetMap


class TestMapLocations:
    """Class that tests OSM locations"""

    def setup_class(self):
        self.map = OpenStreetMap()

    def test_get_places_location(self, monkeypatch):
        places = ([48.8534, 45.764043],
                  [2.3488, 4.835659],
                  ["18, rue de Lyon, Paris", "144 av. du Maine, Paris"])

        class MockRequestResponse:
            status_code = 200

            @staticmethod
            def json():
                return [{
                    "lat": 48.8534,
                    "lon": 2.3488,
                    "display_name": "18, rue de Lyon, Paris",
                    "address": {"municipality": "Paris"}
                },
                    {
                        "lat": 45.764043,
                        "lon": 4.835659,
                        "display_name": "144 av. du Maine, Paris",
                        "address": {"municipality": "Paris"}
                    }]

        def mockreturn(*args):
            mockreturn.params = {"args": args}
            response = MockRequestResponse
            return response

        monkeypatch.setattr("requests.get", mockreturn)

        assert self.map.get_places_location("Paris") == places

        assert MockRequestResponse.status_code == 200
