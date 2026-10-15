from django.test import TestCase, Client
from django.urls import reverse
from satTrack.models import Satellite

class ProductionRouteSmokeTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Seed test satellite if needed
        self.sat = Satellite.objects.create(
            norad_id=25544,
            name="ISS (ZARYA)",
            tle_now="1 25544U 98067A   26001.00000000  .00016717  00000-0  10270-3 0  9002\n2 25544  51.6400 208.5000 0005000 130.0000 325.0000 15.50000000    11"
        )

    def test_healthz_endpoint(self):
        response = self.client.get('/healthz')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok", "app": "satvex"})

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_satellite_list_page(self):
        response = self.client.get('/sat')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_pass_predictor_page(self):
        response = self.client.get('/pass-predictor')
        self.assertEqual(response.status_code, 200)

    def test_multi_viewer_page(self):
        response = self.client.get('/multi-viewer')
        self.assertEqual(response.status_code, 200)

    def test_comparison_page(self):
        response = self.client.get('/comparison')
        self.assertEqual(response.status_code, 200)

    def test_tle_comparison_page(self):
        response = self.client.get('/tle-comparison')
        self.assertEqual(response.status_code, 200)

    def test_satellite_api_list(self):
        response = self.client.get('/api/satellites/list')
        self.assertEqual(response.status_code, 200)
