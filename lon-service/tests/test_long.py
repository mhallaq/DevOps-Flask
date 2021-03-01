# import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask import Flask
from app import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestLongitude(TestBase):
    def test_longitude(self):
    # We will mock a response of 1 and test that we get football returned.
        response = self.client.get(url_for('get_lon'))
        self.assertEqual(response.status_code, 200)
           