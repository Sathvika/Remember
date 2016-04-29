'''
DB management
'''
from app import db, dest
import os

db.drop_all()
filelist = [ f for f in os.listdir(dest) ]
for f in filelist:
    print f
    os.remove(f)
db.create_all()
print "reset db"
