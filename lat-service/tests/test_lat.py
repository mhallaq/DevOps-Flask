from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask import Flask
from app import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestLatitude(TestBase):
    def test_latitude(self):
        response = self.client.get(url_for('get_lat'))
        self.assertEqual(response.status_code, 200)