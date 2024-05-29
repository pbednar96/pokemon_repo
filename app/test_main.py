import unittest
from main import app, PokemonOpenAI
from unittest.mock import patch

pokemon_openai = PokemonOpenAI()


class TestStructuredDataEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('pokemon_openai.get_response_openai')
    def test_missing_data(self, mock_get_response):
        response = self.app.post('/structured', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input', response.json['error'])

    @patch('pokemon_openai.get_response_openai')
    def test_missing_text_key(self, mock_get_response):
        response = self.app.post('/structured', json={"foo": "bar"})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input', response.json['error'])

    @patch('pokemon_openai.get_response_openai', return_value={"text": "Pokemon data"})
    def test_successful_response(self, mock_get_response):
        mock_response = {"pokemon_name": "Pokemon"}
        mock_get_response.return_value = mock_response
        response = self.app.post('/structured', json={"text": "Pokemon data"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_response)


if __name__ == '__main__':
    unittest.main()
