#Model
from flask_login import UserMixin
from Controler import db #import db variable from controler

#User model
class User(UserMixin, db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(45), index=True, unique=True)
    password = db.Column(db.String(45))


    def get_id(self):
        return (self.id)
    
class Tasks(db.Model):
    __tablename__ = "Tasks"
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(45))
    task_assignee = db.Column(db.String(45))
    #due_date = db.Column
    
    