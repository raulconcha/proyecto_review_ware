from django.test import TestCase
from django.test import Client



class ViewsTest(TestCase):
    def test_index_loads_properly(self):
        """La página raíz se carga correctamente"""
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)


class ViewTestLogin(TestCase):
    def test_requerimientos_url(self):
        """La página de login se carga correctamente"""
        c = Client()
        resp = c.get('http://localhost:8000/login/')
        self.assertEqual(resp.status_code, 200)