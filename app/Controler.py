#Controler (it handles connection to DB )
from flask import Flask,render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

App = Flask(__name__) #creates one instance of FLask class

@App.route("/")
def index():
    return render_template('index.html')

# Creating DB
#db = SQLAlchemy(App)

#login = LoginManager(App)
#App.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/CRUD-app-DB'

if __name__ == "__main__":
    App.run(debug=True)