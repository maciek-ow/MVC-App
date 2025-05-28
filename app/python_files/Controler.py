#Controler (it handles connection to DB )
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import psycopg

App = Flask(__name__) #creates one instance of FLask class
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate(App, db)
def create_app():

    #Creating DB
    App.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@localhost:5432/crud_app"

    App.secret_key = "SECRET"

    # Initialazie extensions
    db.init_app(App)
    login_manager.init_app(App)
    login_manager.login_view = "login"

    from python_files.View import init_routes
    init_routes(App)
    
    return App

def connect():
    connection = psycopg.connect("dbname='crud_app' user='admin' host='localhost' password='admin'")
    return connection