import requests
import unittest
import json

URL = 'http://127.0.0.1:8080/betriebsstelle/aamp'
response = requests.get(URL)
response.encoding = 'UTF-8'

class TestRestAPI(unittest.TestCase):
    def testStatusCode(self):
        self.assertEqual(response.status_code, 200)

    def testResponse(self):
        file = open('tests/aamp.json', encoding='utf-8')
        expectedResponses = json.load(file)
        self.assertEqual(expectedResponses['Kurzname'], response.json()['Kurzname'])
        file.close()

if __name__ == '__main__':
    unittest.main()