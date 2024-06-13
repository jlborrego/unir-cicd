import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    #Methods return correct results
    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_square(self):
        url = f"{BASE_URL}/calc/square/25"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_logarithm(self):
        url = f"{BASE_URL}/calc/logarithm/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    #Methods fail with zero par
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400, f"Se esperaba un código de estado 400, pero se recibió {e.code}")
        else:
            self.fail(f"Se esperaba una excepción HTTPError con código 400, pero la petición fue exitosa con código {response.status}")
    
    
    def test_api_logarithm_by_zero(self):
        url = f"{BASE_URL}/calc/logarithm/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400, f"Se esperaba un código de estado 400, pero se recibió {e.code}")
        else:
            self.fail(f"Se esperaba una excepción HTTPError con código 400, pero la petición fue exitosa con código {response.status}")
  
    #Methods fail with negative par
    def test_api_logarithm_by_negative(self):
        url = f"{BASE_URL}/calc/logarithm/-1"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400, f"Se esperaba un código de estado 400, pero se recibió {e.code}")
        else:
            self.fail(f"Se esperaba una excepción HTTPError con código 400, pero la petición fue exitosa con código {response.status}")
  
    def test_api_square_by_negative(self):
        url = f"{BASE_URL}/calc/square/-1"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(e.code, 400, f"Se esperaba un código de estado 400, pero se recibió {e.code}")
        else:
            self.fail(f"Se esperaba una excepción HTTPError con código 400, pero la petición fue exitosa con código {response.status}")
  
