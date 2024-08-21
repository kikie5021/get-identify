import unittest
from app import create_app

class BasicTests(unittest.TestCase):
    def setUp(self):
        # creates a test client
        app = create_app()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_main_page(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
