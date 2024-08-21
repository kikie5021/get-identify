import unittest
from flask import Flask, request
from app import create_app  # ตรวจสอบวิธีการสร้างแอป Flask ในโค้ดของคุณ

class ViewTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the app."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        """Tear down any data after tests are complete."""
        # ล้างข้อมูลทดสอบหรือปิด resources
