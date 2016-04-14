from app import db
from datetime import datetime


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300))
    date = db.Column(db.DateTime)
    user = db.Column(db.String(20))  # id int?

    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.date = datetime.today()

    def __repr__(self):
        return '<Content %r , User %r>' % (self.content, self.user)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = datetime.today()

    def __repr__(self):
        return '<Username %r>' % (self.username)
