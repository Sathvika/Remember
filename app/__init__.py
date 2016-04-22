from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
import flask.ext.login as flask_login
import os

app = Flask(__name__)
app.secret_key = 'super secret string'
=======
import os

app = Flask(__name__)
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec

#set up database
user = 't8tqsg2cy22gsoid'
password = 'jwna145twvabjckt'
host = 'bqmayq5x95g1sgr9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
dbname = 'nss6p3d5ap6mnznd'
SQLALCHEMY_DATABASE_URI = 'mysql://'+user+':'+password+'@'+host+':3306/'+dbname
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

<<<<<<< HEAD
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import rememberApp, models

db.create_all()

=======
from app import rememberApp, models

db.create_all()
>>>>>>> 5e0aa7209ae5a1a3b9959f54ab7946782ddd36ec
