import unittest
import json
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_endpoint(self):
        response = self.client.get('/api/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello World!"})

    def test_add_endpoint(self):
        payload = json.dumps({
            "number_1": 5,
            "number_2": 3
        })
        response = self.client.post('/api/add',
                                    data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    def test_multiply_endpoint(self):
        payload = json.dumps({
            "number_1": 4,
            "number_2": 5
        })
        response = self.client.post('/api/multiply', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 20})

    def test_subtract_endpoint(self):
        payload = json.dumps({
            "number_1": 8,
            "number_2": 3
        })
        response = self.client.post('/api/subtract', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 5})

    def test_divide_endpoint(self):
        payload = json.dumps({
            "number_1": 9,
            "number_2": 3
        })
        response = self.client.post('/api/divide', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 3})

    def test_divide_by_zero(self):
        payload = json.dumps({
            "number_1": 9,
            "number_2": 0
        })
        response = self.client.post('/api/divide', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Division by zero"})

    def test_sqrt_endpoint(self):
        payload = json.dumps({
            "number": 16
        })
        response = self.client.post('/api/sqrt', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 4})

    def test_power_endpoint(self):
        payload = json.dumps({
            "base": 2,
            "exponent": 3
        })
        response = self.client.post('/api/power', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    def test_trigonometric_sin(self):
        payload = json.dumps({
            "function": "sin",
            "angle": 90
        })
        response = self.client.post('/api/trig', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json["result"], 1.0, places=1)

    def test_logarithm_endpoint(self):
        payload = json.dumps({
            "number": 10
        })
        response = self.client.post('/api/log', data=payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json["result"], 2.302585, places=6)

if __name__ == '__main__':
    unittest.main()
