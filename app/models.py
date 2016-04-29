from app import db
from datetime import datetime


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300))
    date = db.Column(db.DateTime)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    url = db.Column(db.String(100), default="http://i.imgur.com/nSwnHBm.jpg")

    def __init__(self, content, user, url):
        self.content = content
        self.user = user
        self.date = datetime.today()
        self.url = url

    def __repr__(self):
        return '<Content %r , User %r>' % (self.content, self.user)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    children = db.relationship("Content")

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = datetime.today()

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Username %r>' % self.username


class Settings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    displayName = db.Column(db.String(20))
    notificationTime = db.Column(db.DateTime)
    notification = db.Column(db.Boolean, default=False)
    public = db.Column(db.Boolean, default=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, time, notifications, public, user):
        self.displayName = name
        self.notificationTime = time
        self.notification = notifications
        self.public = public
        self.user = user

    def __repr__(self):
        return '<displayName %r , notificationTime %r, notifications on %r, public posts %r>' % \
               (self.displayName, self.notificationTime, self.notification, self.public)


class Photo(db.Model):
    __tablename__ = 'Photo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(30))
    user = db.Column(db.String(20))
    url = db.Column(db.String(100))

    def __init__(self, filename, user, url):
        self.filename = filename
        self.user = user
        self.url = url

    def __repr__(self):
        return '<Filename %r, Username %r, URL %r>' % (self.filename, self.user, self.url)
