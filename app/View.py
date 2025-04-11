#View
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from Controler import App
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request, flash, session
from Model import User

class LoginForm(FlaskForm):
    username = StringField('Username', validator=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired])
    submit = SubmitField('Sign in')

### LOGIN LOGOUT STUFF ###

@App.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    #get form data
    form_username = form.username.data
    form_password= form.password.data

    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form_username).first()
        password = user.password
        if user is None or password != form_password:
            flash('Invalid username or password')
            return redirect(url_for(login))
        login_user(user)
        session.permanent = True
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
@App.route("/logut")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))