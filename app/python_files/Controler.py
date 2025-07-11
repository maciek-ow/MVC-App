#Controler (it handles connection to DB )
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import psycopg2
import os

App = Flask(__name__) #creates one instance of FLask class
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate(App, db)
def create_app():

    App = Flask(__name__,
                 template_folder='../templates',
                 static_folder='../static')
    
    #Creating DB
    App.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", 
        "postgresql://admin:admin@db:5432/crud_app"  # Changed from localhost to 'db'
    )
    App.secret_key = os.getenv("SECRET_KEY", "SECRET")

    # Initialazie extensions
    db.init_app(App)
    login_manager.init_app(App)
    login_manager.login_view = "login"

    from python_files.View import init_routes
    init_routes(App)
    
    return App

def connect():
    connection = psycopg2.connect(
    dbname='crud_app',
    user='admin',
    host='db', 
    password='admin'
    )
    return connection