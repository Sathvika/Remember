<<<<<<< HEAD
"""
Testing an API is hard...
"""
import unittest
from app import db, models
import requests
from requests_futures.sessions import FuturesSession
import json
=======
import unittest
from app import db, models
import requests
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec

class MyTest(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

<<<<<<< HEAD
    def testGetPosts(self):
        #there shouldn't be anything there because it's a fresh db
        r = requests.get('https://cs242project.herokuapp.com/getPosts')
        res = r.json()
        self.assertEqual(res['data'], [])

    def testPost(self):
        newPost = json.dumps({'content':'testing'})
        res = requests.post('https://cs242project.herokuapp.com/submitPost', data=newPost)
        print res.json()

    def testMakePosts(self):
        s = FuturesSession()
        newPost = json.dumps({'content':'testing'})
        print newPost
        p = s.post('https://cs242project.herokuapp.com/submitPost', data=newPost)
        res = p.result()
        print res
        print res.content
        r = s.get('https://cs242project.herokuapp.com/getPosts')
        res2 = r.result()
        print res2.content
=======
    def testPost(self):
        requests.get('/submitPost')
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec
        self.assertEqual("test", "test")