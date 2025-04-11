#View
from flask_login import LoginManager, login_user, logout_user, login_required
from Controler import login #imports app variable from controller




login_manager = LoginManager()

#this method is used to as part of the flask_login code.
#@login_manager.login.user_loader
#def load_user(id):
    #return user.query.get(int(id)) #returns user id to use in any place in the code

