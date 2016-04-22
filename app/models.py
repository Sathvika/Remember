from app import db
from datetime import datetime


class Content(db.Model):
<<<<<<< HEAD
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300))
    date = db.Column(db.DateTime)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
=======
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(300))
    date = db.Column(db.DateTime)
    user = db.Column(db.String(20))  # id int?
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec

    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.date = datetime.today()

    def __repr__(self):
        return '<Content %r , User %r>' % (self.content, self.user)


class User(db.Model):
<<<<<<< HEAD
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    children = db.relationship("Content")

    # authenticated = db.Column(db.Boolean, default=False)
=======
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.date = datetime.today()

<<<<<<< HEAD
    # @property
    def is_authenticated(self):
        return self.authenticated

    # @property
    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return '<Username %r>' % (self.username)


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
        return '<displayName %r , notificationTime %r, notifications on %r, public posts %r>' %\
               (self.displayName, self.notificationTime, self.notification, self.public)
=======
    def __repr__(self):
        return '<Username %r>' % (self.username)
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec
