#Controler (it handles connection to DB )
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


App = Flask(__name__) #creates one instance of FLask class

 #Creating DB
App.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@localhost:5432/CRUD-app-DB"

# Initialazie extensions
db = SQLAlchemy(App)
login = LoginManager(App)

@login.user_loader
def load_user(id):
    from Model import User
    return User.query.get(int(id)) #returns user id to use in any place in the code

@App.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    App.run(debug=True)