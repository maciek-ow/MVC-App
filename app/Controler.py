#Controler (it handles connection to DB )
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
def create_app():

    App = Flask(__name__) #creates one instance of FLask class

    #Creating DB
    App.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@localhost:5432/CRUD-app-DB"

    App.secret_key = "SECRET"

    # Initialazie extensions
    db.init_app(App)
    login_manager.init_app(App)
    login_manager.login_view = "login"

    from View import init_routes
    init_routes(App)
    
    return App