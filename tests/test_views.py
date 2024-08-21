import unittest
from app import app

class ViewTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the app for testing
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page(self):
        # Test the login page access and the form
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login', response.data.decode())

    def test_dashboard_access(self):
        # Test access to dashboard
        with self.app.session_transaction() as session:
            session['logged_in'] = True
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Dashboard', response.data.decode())

if __name__ == '__main__':
    unittest.main()
