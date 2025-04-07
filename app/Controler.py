#Controler (it handles connection to DB )
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

App = Flask(__name__) #creates one instance of FLask class

# Creating DB
db = SQLAlchemy(App)

login = LoginManager(App)
App.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/CRUD-app-DB'

if __name__ == "__main__":
    App.run(debug=True)