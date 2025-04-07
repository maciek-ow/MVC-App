#Model
from flask_login import UserMixin
from Controler import db #import db variable from controler
from View import login #import login variable from View

@login.user_loader
def load_user(id):
    return User.query.get(int(id)) #returns user id to use in any place in the code

#User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(45), index=True, unique=True)
    password = db.Column(db.String(45))

    def get_id(self):
        return (self.id)