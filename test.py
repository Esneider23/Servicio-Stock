import unittest
import requests


class BasicTest(unittest.TestCase):

    def index(self):
        URL = 'https://servicio-stock.onrender.com/vehicles'
        res = requests.get(self.URL)
        self.assertEqual(res.status_code, 200)


if __name__ == '_main_':
    unittest.main()
