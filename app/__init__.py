from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask.ext.login as flask_login
import flask.ext.uploads as flask_uploads
import os

app = Flask(__name__)
app.secret_key = 'super secret string'

'''
Set up database
'''
user = 't8tqsg2cy22gsoid'
password = 'jwna145twvabjckt'
host = 'bqmayq5x95g1sgr9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
dbname = 'nss6p3d5ap6mnznd'
SQLALCHEMY_DATABASE_URI = 'mysql://' + user + ':' + password + '@' + host + ':3306/' + dbname
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

'''
Flask-login
'''
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

'''
Flask-uploads
'''
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

dest = os.path.join(APP_ROOT, 'static/data/')

app.config['UPLOADS_DEFAULT_DEST'] = dest
app.config['UPLOADED_PHOTOS_ALLOW'] = ['png', 'jpg', 'jpeg', 'gif']

photos = flask_uploads.UploadSet('photos', flask_uploads.IMAGES)
flask_uploads.configure_uploads(app, (photos))
flask_uploads.patch_request_class(app, 32 * 1024 * 1024)


from app import views, models, settings, users, posts

db.create_all()
