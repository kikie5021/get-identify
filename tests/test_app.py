import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the app for testing
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test the home page access
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome', response.data.decode())

    def test_error_page(self):
        # Test for error page response
        response = self.app.get('/path-not-exist')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
