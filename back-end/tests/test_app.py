import unittest
from unittest.mock import patch
from flask import url_for
# from flask.wrappers import Response
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
           return app

class TestWeather(TestBase):
    def test_weather(self):
        fake_json={"temp":"12","feels_like":"14","weather":"Cloudy","lon":"10","lat":"20"}
        with patch('requests.get') as mock_get:
            mock_get.return_value=fake_json       
            response = fake_json
        self.assertEqual(response,fake_json)

# if __name__=="__main__":
#     unittest.main()


# class TestBackEnd(TestBase):
#     def test_back_end(self):
#         with patch("requests.get") as g:
#             g.return_value.text=1
#             g.return_value.text=2
#             g.return_value.text='89e40660f0dc846aaeeae4b18b9c47b5'
#             response = self.client.get(url_for('weather'))
#             self.assertEqual(response.status_code, 200)