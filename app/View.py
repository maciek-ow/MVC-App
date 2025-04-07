#View
from flask import render_template, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, login_required
from Controler import App #imports app variable from controller

 #

login_manager = LoginManager()
login_manager.init.app(App)

#this method is used to as part of the flask_login code.
@login_manager.login.user_loader
#def load_user(id):
    #return user.query.get(int(id)) #returns user id to use in any place in the code

@App.route('/')
def index():
    return render_template('index.html')