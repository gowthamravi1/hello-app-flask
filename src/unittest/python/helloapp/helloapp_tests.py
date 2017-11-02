from flask import url_for
import unittest

from webapp import application

class HelloAppTest(unittest.TestCase):
    
    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """Assert that user successfully lands on homepage"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()