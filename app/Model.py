#Model
from flask_login import UserMixin
from app import db, login
#USER MODEL#

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model): #User
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))