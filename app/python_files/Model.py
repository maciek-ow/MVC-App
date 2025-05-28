#Model
from flask_login import UserMixin
from python_files.Controler import db #import db variable from controler
from enum import Enum

#User model
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(45), index=True, unique=True)
    password = db.Column(db.String(45))


    def get_id(self):
        return (self.id)
    
class TaskStatus(Enum):
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'
    
class Tasks(db.Model):
    __tablename__ = "Tasks"
    __table_args__ = {'schema': 'new_schema'} 
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(45))
    task_assignee = db.Column(db.String(45))
    task_due_date = db.Column(db.Date)
    status = db.Column(db.String(20), default=TaskStatus.TODO.value)
    
    user_id =db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User', backref='tasks')
    
