import unittest
import requests


class TestAppi(unittest.TestCase):
    URL = "https://servicio-stock.onrender.com/vehiculos"

    def test_1_get_all(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 2)
        print("Test 1 completed")


if __name__ == 'main':
    tester = TestAppi()

    tester.test_1_get_all()
