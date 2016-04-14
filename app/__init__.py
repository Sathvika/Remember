from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#set up database
user = 't8tqsg2cy22gsoid'
password = 'jwna145twvabjckt'
host = 'bqmayq5x95g1sgr9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
dbname = 'nss6p3d5ap6mnznd'
SQLALCHEMY_DATABASE_URI = 'mysql://'+user+':'+password+'@'+host+':3306/'+dbname
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from app import rememberApp, models

db.create_all()