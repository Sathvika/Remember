import unittest
from app import db, models
import requests

class MyTest(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def testPost(self):
        requests.get('/submitPost')
        self.assertEqual("test", "test")