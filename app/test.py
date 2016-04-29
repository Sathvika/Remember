"""
Testing an API is hard...
"""
import unittest
from app import db
import requests
from requests_futures.sessions import FuturesSession
import json


class MyTest(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def testGetPosts(self):
        # there shouldn't be anything there because it's a fresh db
        r = requests.get('https://cs242project.herokuapp.com/getPosts')
        res = r.json()
        self.assertEqual(res['data'], [])

    def testPost(self):
        new_post = json.dumps({'content': 'testing'})
        res = requests.post('https://cs242project.herokuapp.com/submitPost', data=new_post)
        print res.json()

    def testMakePosts(self):
        s = FuturesSession()
        new_post = json.dumps({'content': 'testing'})
        print new_post
        p = s.post('https://cs242project.herokuapp.com/submitPost', data=new_post)
        res = p.result()
        print res
        print res.content
        r = s.get('https://cs242project.herokuapp.com/getPosts')
        res2 = r.result()
        print res2.content
        self.assertEqual("test", "test")
